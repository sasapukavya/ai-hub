from llm.llm import LLM


class RouterAgent:

    def __init__(self):
        self.llm = LLM()

    def route(self, question):

        system_prompt = """
You are a routing agent.

Return ONLY valid JSON.

Example:
{
    "agent": "employee"
}

Available agents:
- employee
- general
"""

        response = self.llm.invoke_json(
            system_prompt,
            question
        )

        return response