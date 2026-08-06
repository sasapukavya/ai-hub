from database.feedback_db import get_feedback


def get_statistics():
    feedback = get_feedback()

    total = len(feedback)

    approved = sum(
        1 for item in feedback
        if item["approved"]
    )

    rejected = total - approved

    if total == 0:
        approval_rate = 0
    else:
        approval_rate = round(
            approved / total * 100,
            2
        )

    return {
        "total": total,
        "approved": approved,
        "rejected": rejected,
        "approval_rate": approval_rate
    }