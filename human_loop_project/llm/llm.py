import os
import json

from dotenv import load_dotenv
from openai import OpenAI


# Load environment variables
load_dotenv()


# Get OpenRouter details

API_KEY = os.getenv("OPENROUTER_API_KEY")

MODEL = os.getenv(
    "MODEL",
    "qwen/qwen-2.5-7b-instruct:free"
)


# Debug information

print("\n==============================")
print("LLM CONFIGURATION")
print("==============================")
print("Model:", MODEL)

if API_KEY:
    print("API Key: Loaded")
else:
    print("API Key: Missing")

print("==============================\n")



# OpenRouter Client

client = OpenAI(

    api_key=API_KEY,

    base_url="https://openrouter.ai/api/v1"

)



class LLM:


    def invoke(
        self,
        system_prompt: str,
        user_prompt: str
    ):

        """
        Normal text response
        """

        try:

            response = client.chat.completions.create(

                model=MODEL,

                messages=[

                    {
                        "role": "system",
                        "content": system_prompt
                    },

                    {
                        "role": "user",
                        "content": user_prompt
                    }

                ],

                temperature=0

            )


            return (
                response
                .choices[0]
                .message
                .content
            )


        except Exception as e:


            print("\n❌ LLM ERROR")
            print(e)


            return (
                "Sorry, the AI service is "
                "temporarily unavailable."
            )



    def invoke_json(
        self,
        system_prompt: str,
        user_prompt: str
    ):

        """
        JSON response for Agents
        Example:

        {
            "tool":"calculator",
            "tool_input":"20*5"
        }

        """

        try:


            response = client.chat.completions.create(

                model=MODEL,


                messages=[

                    {
                        "role":"system",
                        "content":system_prompt
                    },

                    {
                        "role":"user",
                        "content":user_prompt
                    }

                ],


                temperature=0

            )


            content = (
                response
                .choices[0]
                .message
                .content
            )


            # Remove markdown JSON blocks if returned

            content = content.replace(
                "```json",
                ""
            )

            content = content.replace(
                "```",
                ""
            )


            return json.loads(
                content.strip()
            )



        except Exception as e:


            print("\n❌ JSON LLM ERROR")
            print(e)


            # Safe fallback

            return {

                "tool": "calculator",

                "tool_input": "0"

            }