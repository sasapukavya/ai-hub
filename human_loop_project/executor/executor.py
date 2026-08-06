from llm.llm import LLM
from tools.registry import TOOLS


class Executor:

    def __init__(self):

        self.llm = LLM()

    def execute(self, plan: dict):

        # General Agent doesn't need any tool
        if plan["agent"] == "GENERAL":

            return {
                "success": True,
                "answer": plan["response"]
            }

        tool_name = plan["tool"]

        tool_input = plan["tool_input"]

        if tool_name not in TOOLS:

            return {
                "success": False,
                "answer": f"Unknown tool: {tool_name}"
            }

        tool_function = TOOLS[tool_name]

        tool_result = tool_function(tool_input)

        final_prompt = f"""
You are a helpful AI assistant.

User Question:
{plan["question"]}

Tool Used:
{tool_name}

Tool Output:
{tool_result}

Generate a professional and easy-to-understand answer.

Do not mention internal tool names.
"""

        final_answer = self.llm.invoke(
            "You are a helpful assistant.",
            final_prompt
        )

        return {
            "success": True,
            "answer": final_answer,
            "tool_result": tool_result
        }