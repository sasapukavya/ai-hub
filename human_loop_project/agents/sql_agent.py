from llm.llm import LLM
from prompts.sql_prompt import SQL_PROMPT



class SQLAgent:


    def __init__(self):

        self.llm = LLM()



    def run(self, question):


        result = self.llm.invoke_json(

            SQL_PROMPT,

            question

        )


        return result