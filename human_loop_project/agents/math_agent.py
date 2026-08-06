from llm.llm import LLM
from prompts.math_prompt import MATH_PROMPT


class MathAgent:

    def __init__(self):

        self.llm = LLM()

    def run(self, question):

        result = self.llm.invoke_json(

            MATH_PROMPT,

            question

        )

        return {

            "tool": "calculator",

            "tool_input": result["expression"]

        }