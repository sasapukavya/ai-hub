def human_approval(state):

    print()

    print("Question")

    print(state["question"])

    print()

    print("Selected Tool")

    print(state["tool_name"])

    print()

    print("Tool Input")

    print(state["tool_input"])

    print()

    decision = input("Approve? (yes/no): ")

    state["approved"] = decision.lower() == "yes"

    return state