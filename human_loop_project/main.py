from workflow.graph import workflow

while True:

    question=input("\nYou: ")

    if question=="exit":

        break

    state={

        "question":question,

        "agent":"",

        "tool_name":"",

        "tool_input":"",

        "tool_output":"",

        "approved":False,

        "final_answer":""

    }

    result=workflow.invoke(state)

    print()

    print("="*60)

    print(result["final_answer"])