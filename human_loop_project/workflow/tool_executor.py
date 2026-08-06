from tools.registry import TOOLS


def execute_tool(state):

    tool = state["tool_name"]

    tool_input = state["tool_input"]

    result = TOOLS[tool](tool_input)

    state["tool_output"] = str(result)

    return state