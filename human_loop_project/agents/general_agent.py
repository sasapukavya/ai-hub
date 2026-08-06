from llm.llm import LLM


class GeneralAgent:


    def __init__(self):

        self.llm = LLM()



    def run(self, question):


        response = self.llm.invoke(

            "You are a helpful general AI assistant. Answer clearly.",

            question

        )


        return response