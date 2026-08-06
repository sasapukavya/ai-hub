from planner.planner import Planner


def main():

    planner = Planner()


    questions = [

        "Calculate 50 * 10",

        "Show employees with salary above 70000",

        "Explain machine learning"

    ]


    for question in questions:


        print("\n\n==============================")

        print("USER QUESTION")

        print(question)


        plan = planner.create_plan(question)


        print("\nGENERATED PLAN")

        print(plan)

        print("==============================")



if __name__ == "__main__":
    main()