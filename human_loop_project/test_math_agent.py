from agents.math_agent import MathAgent

agent = MathAgent()

while True:

    question = input("\nQuestion: ")

    if question.lower() == "exit":

        break

    result = agent.run(question)

    print()

    print(result)

    print()