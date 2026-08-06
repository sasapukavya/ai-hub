from llm.llm import LLM


def main():

    llm = LLM()

    response = llm.invoke(
        "You are a helpful AI assistant.",
        "What is artificial intelligence?"
    )

    print("\n==============================")
    print("LLM RESPONSE")
    print("==============================\n")

    print(response)


if __name__ == "__main__":
    main()