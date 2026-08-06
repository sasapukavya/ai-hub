from database.feedback_db import get_feedback


class Memory:

    def search(self, question):
        """
        Returns the first matching approved feedback.
        """

        feedback = get_feedback()

        for item in feedback:

            if (
                item.get("approved", False)
                and item["question"].lower() == question.lower()
            ):
                return item

        return None

    def get_best_plan(self, question):
        """
        Returns a planner-compatible plan if an approved
        question already exists.
        """

        previous = self.search(question)

        if previous is None:
            return None

        return {
            "question": previous["question"],
            "agent": previous["agent"],
            "tool": previous.get("tool"),
            "tool_input": previous.get("tool_input"),
            "response": previous.get("response"),
            "reason": "Loaded from previous approved feedback.",
            "confidence": 100,
            "requires_approval": False,
            "from_memory": True
        }

    def get_all_feedback(self):
        """
        Returns all stored feedback.
        """

        return get_feedback()