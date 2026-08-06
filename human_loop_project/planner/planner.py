from agents.supervisor import decide_agent

from agents.math_agent import MathAgent
from agents.sql_agent import SQLAgent
from agents.general_agent import GeneralAgent


class Planner:

    def __init__(self):

        self.math_agent = MathAgent()
        self.sql_agent = SQLAgent()
        self.general_agent = GeneralAgent()

    def create_plan(self, question):

        agent = decide_agent(question)

        print("\n" + "=" * 60)
        print("PLANNER")
        print("=" * 60)
        print("Question :", question)
        print("Selected Agent :", agent)
        print("=" * 60)

        # ==========================================================
        # MATH AGENT
        # ==========================================================

        if agent == "MATH":

            result = self.math_agent.run(question)

            plan = {
                "question": question,
                "agent": "MATH",
                "tool": result["tool"],
                "tool_input": result["tool_input"],
                "response": None,
                "reason": "The question requires mathematical calculation.",
                "confidence": 0.98,
                "requires_approval": True
            }

        # ==========================================================
        # SQL AGENT
        # ==========================================================

        elif agent == "SQL":

            result = self.sql_agent.run(question)

            plan = {
                "question": question,
                "agent": "SQL",
                "tool": result["tool"],
                "tool_input": result["tool_input"],
                "response": None,
                "reason": "The question requires database or SQL operations.",
                "confidence": 0.97,
                "requires_approval": True
            }

        # ==========================================================
        # GENERAL AGENT
        # ==========================================================

        else:

            result = self.general_agent.run(question)

            plan = {
                "question": question,
                "agent": "GENERAL",
                "tool": None,
                "tool_input": None,
                "response": result,
                "reason": "The question is a general knowledge or conversational request.",
                "confidence": 0.95,
                "requires_approval": True
            }

        print("\nGenerated Plan")
        print("-" * 60)
        print(plan)
        print("=" * 60)

        return plan