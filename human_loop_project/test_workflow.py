from workflow.graph import workflow


state = {

    "question": "Calculate 25 multiplied by 10",

    "agent": "",

    "tool_name": "",

    "tool_input": "",

    "tool_output": "",

    "approved": False,

    "final_answer": ""

}

result = workflow.invoke(state)

print()

print(result)