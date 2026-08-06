from llm.llm import LLM
from prompts.supervisor_prompt import SUPERVISOR_PROMPT


llm = LLM()



def decide_agent(question: str):


    response = llm.invoke(

        SUPERVISOR_PROMPT,

        question

    )


    response = response.strip().upper()


    if "MATH" in response:

        return "MATH"


    elif "SQL" in response:

        return "SQL"


    else:

        return "GENERAL"