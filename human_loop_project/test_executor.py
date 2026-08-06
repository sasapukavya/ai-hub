from planner.planner import Planner
from executor.executor import Executor



def main():

    planner = Planner()

    executor = Executor()


    while True:


        question = input("\nAsk Question: ")


        if question.lower() == "exit":

            break



        # Step 1: Create plan

        plan = planner.create_plan(question)


        print("\n==============================")

        print("AI PLAN")

        print("==============================")

        print(plan)



        # Step 2: Human Approval


        if plan["requires_approval"]:


            choice = input(
                "\nApprove execution? (yes/no): "
            )


            if choice.lower() != "yes":

                print(
                    "\n❌ Execution rejected by human"
                )

                continue



        # Step 3: Execute


        result = executor.execute(plan)



        print("\n==============================")

        print("FINAL ANSWER")

        print("==============================")

        print(result["answer"])




if __name__ == "__main__":
    main()