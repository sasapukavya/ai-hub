from typing import TypedDict


class AgentState(TypedDict):

    question: str

    agent: str

    tool_name: str

    tool_input: str

    tool_output: str

    final_answer: str

    approved: bool