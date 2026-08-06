from tools.calculator_tool import CalculatorTool
from tools.database_tool import DatabaseTool


calculator = CalculatorTool()

database = DatabaseTool()



TOOLS = {

    "calculator":
        calculator.calculate,


    "database":
        database.query

}