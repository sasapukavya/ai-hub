from langgraph.graph import StateGraph, END

from workflow.state import AgentState

from workflow.nodes import (
    supervisor_node,
    routing_node
)


builder = StateGraph(AgentState)

builder.add_node(
    "supervisor",
    supervisor_node
)

builder.add_node(
    "routing",
    routing_node
)

builder.set_entry_point("supervisor")

builder.add_edge(
    "supervisor",
    "routing"
)

builder.add_edge(
    "routing",
    END
)

workflow = builder.compile()