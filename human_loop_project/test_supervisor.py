from agents.supervisor import decide_agent


def main():

    questions = [

        "Calculate 25 multiplied by 20",

        "Show employees earning more than 70000",

        "Who invented Python?"

    ]


    for question in questions:

        agent = decide_agent(question)


        print("\n==============================")

        print("Question:")
        print(question)

        print()

        print("Selected Agent:")
        print(agent)

        print("==============================")



if __name__ == "__main__":
    main()