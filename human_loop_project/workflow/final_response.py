from llm.llm import LLM

llm = LLM()


def generate_answer(state):

    answer = llm.invoke(

        "You are a helpful assistant.",

        f"""

User Question

{state["question"]}

Tool Output

{state["tool_output"]}

Generate a helpful response.

"""

    )

    state["final_answer"] = answer

    return state