from agents.sql_agent import SQLAgent



agent = SQLAgent()


result = agent.run(
    "Show employees earning above 70000"
)


print(result)