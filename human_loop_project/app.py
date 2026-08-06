import streamlit as st
from datetime import datetime

from planner.planner import Planner
from executor.executor import Executor
from memory.memory import Memory

from database.feedback_db import save_feedback
from database.analytics import get_statistics


# ==========================================================
# Logger
# ==========================================================

def add_log(message):

    timestamp = datetime.now().strftime("%H:%M:%S")

    if "system_logs" not in st.session_state:
        st.session_state.system_logs = []

    st.session_state.system_logs.append(
        f"[{timestamp}] {message}"
    )


# ==========================================================
# Page Config
# ==========================================================

st.set_page_config(
    page_title="Human-in-the-Loop AI",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 Human-in-the-Loop Multi Agent AI")


# ==========================================================
# Session State
# ==========================================================

if "planner" not in st.session_state:
    st.session_state.planner = Planner()

if "executor" not in st.session_state:
    st.session_state.executor = Executor()

if "memory" not in st.session_state:
    st.session_state.memory = Memory()

if "messages" not in st.session_state:
    st.session_state.messages = []

if "pending_plan" not in st.session_state:
    st.session_state.pending_plan = None

if "current_question" not in st.session_state:
    st.session_state.current_question = ""

if "approval_logs" not in st.session_state:
    st.session_state.approval_logs = []

if "system_logs" not in st.session_state:
    st.session_state.system_logs = []


# ==========================================================
# Sidebar
# ==========================================================

with st.sidebar:

    st.header("📊 Dashboard")

    try:

        feedback = st.session_state.memory.get_all_feedback()

        total = len(feedback)

        approved = sum(
            1 for item in feedback
            if item["approved"]
        )

        rejected = total - approved

        approval_rate = (
            approved / total * 100
            if total > 0 else 0
        )

        st.metric(
            "Approved",
            approved
        )

        st.metric(
            "Rejected",
            rejected
        )

        st.metric(
            "Approval Rate",
            f"{approval_rate:.1f}%"
        )

    except Exception:

        st.warning("Analytics unavailable")

    st.divider()

    stats = get_statistics()

    st.subheader("Feedback Database")

    st.metric(
        "Total Requests",
        stats["total"]
    )

    st.metric(
        "Approved",
        stats["approved"]
    )

    st.metric(
        "Rejected",
        stats["rejected"]
    )

    st.metric(
        "Approval %",
        f"{stats['approval_rate']}%"
    )

    st.divider()

    if st.button("🗑 Clear Chat"):

        st.session_state.messages = []

        st.session_state.pending_plan = None

        st.session_state.current_question = ""

        st.session_state.approval_logs = []

        st.session_state.system_logs = []

        add_log("Conversation cleared")

        st.rerun()


# ==========================================================
# Chat History
# ==========================================================

for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.write(message["content"])

        if "time" in message:

            st.caption(message["time"])
            # ==========================================================
# User Input
# ==========================================================

question = st.chat_input("Ask your question...")

if question:

    st.session_state.current_question = question

    st.session_state.messages.append(
        {
            "role": "user",
            "content": question,
            "time": datetime.now().strftime("%H:%M")
        }
    )

    add_log(f"User: {question}")

    # ------------------------------------------------------
    # Search Memory
    # ------------------------------------------------------

    previous_plan = st.session_state.memory.search(question)

    if previous_plan:

        add_log("Memory matched a previous approved request.")

        previous_plan["from_memory"] = True

        st.session_state.pending_plan = previous_plan

        st.rerun()

    # ------------------------------------------------------
    # Create Plan
    # ------------------------------------------------------

    plan = st.session_state.planner.create_plan(question)

    add_log(
        f"Planner selected {plan['agent']} Agent"
    )

    st.session_state.pending_plan = plan

    st.rerun()


# ==========================================================
# Human Approval
# ==========================================================

if st.session_state.pending_plan:

    plan = st.session_state.pending_plan

    st.divider()

    st.subheader("🧠 AI Decision")

    st.write("### Selected Agent")
    st.success(plan["agent"])

    if "reason" in plan:
        st.write("### Reason")
        st.info(plan["reason"])

    if "confidence" in plan:

        st.write("### Confidence")

        st.progress(plan["confidence"] / 100)

        st.write(f"{plan['confidence']}%")

    if plan.get("tool"):

        st.write("### Tool")

        st.code(plan["tool"])

        st.write("### Tool Input")

        st.code(str(plan["tool_input"]))

    elif "response" in plan:

        st.write("### AI Response")

        st.info(plan["response"])

    if plan.get("from_memory", False):

        st.success("♻ Using previously approved memory.")
        st.warning("Waiting for Human Approval")

    col1, col2 = st.columns(2)

    with col1:
        approve = st.button("✅ Approve")

    with col2:
        reject = st.button("❌ Reject")

    # ======================================================
    # APPROVE
    # ======================================================

    if approve:

        add_log("Human Approved")

        if plan.get("tool"):

            result = st.session_state.executor.execute(plan)

            answer = result["answer"]

        else:

            answer = plan.get("response", "")

        save_feedback(
            st.session_state.current_question,
            plan,
            True
        )

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": answer,
                "time": datetime.now().strftime("%H:%M")
            }
        )

        st.session_state.approval_logs.append(
            f"✅ {plan['agent']}"
        )

        st.session_state.pending_plan = None

        st.rerun()

    # ======================================================
    # REJECT
    # ======================================================

    if reject:

        add_log("Human Rejected")

        save_feedback(
            st.session_state.current_question,
            plan,
            False
        )

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": "❌ Request rejected by Human.",
                "time": datetime.now().strftime("%H:%M")
            }
        )

        st.session_state.approval_logs.append(
            f"❌ {plan['agent']}"
        )

        st.session_state.pending_plan = None

        st.rerun()


# ==========================================================
# Conversation History
# ==========================================================

if st.session_state.messages:

    st.divider()

    with st.expander("📜 Conversation History", expanded=False):

        for msg in st.session_state.messages:

            if msg["role"] == "user":

                st.markdown(
                    f"**🧑 User:** {msg['content']}"
                )

            else:

                st.markdown(
                    f"**🤖 Assistant:** {msg['content']}"
                )

            if "time" in msg:

                st.caption(msg["time"])


# ==========================================================
# Approval History
# ==========================================================

st.divider()

st.subheader("📋 Approval History")

if len(st.session_state.approval_logs) == 0:

    st.info("No approvals yet.")

else:

    for item in reversed(st.session_state.approval_logs):

        st.write(item)


# ==========================================================
# System Logs
# ==========================================================

st.divider()

with st.expander("⚙️ System Logs", expanded=False):

    if len(st.session_state.system_logs) == 0:

        st.info("No logs available.")

    else:

        for log in reversed(st.session_state.system_logs):

            st.code(log)