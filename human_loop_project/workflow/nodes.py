from agents.supervisor import decide_agent
from agents.math_agent import MathAgent
from agents.sql_agent import SQLAgent
from agents.general_agent import GeneralAgent


math_agent = MathAgent()
sql_agent = SQLAgent()
general_agent = GeneralAgent()


def supervisor_node(state):

    question = state["question"]

    agent = decide_agent(question)

    state["agent"] = agent

    return state


def routing_node(state):

    question = state["question"]

    agent = state["agent"]

    if agent == "MATH":

        result = math_agent.run(question)

        state["tool_name"] = result["tool"]

        state["tool_input"] = result["tool_input"]

        return state

    elif agent == "SQL":

        result = sql_agent.run(question)

        state["tool_name"] = result["tool"]

        state["tool_input"] = result["tool_input"]

        return state

    else:

        result = general_agent.run(question)

        state["final_answer"] = result["response"]

        return state