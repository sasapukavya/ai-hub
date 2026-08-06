import ast
import operator

OPERATORS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.Mod: operator.mod,
    ast.Pow: operator.pow,
    ast.FloorDiv: operator.floordiv,
}


class CalculatorTool:

    def calculate(self, expression: str):

        try:
            tree = ast.parse(expression, mode="eval")

            return self._evaluate(tree.body)

        except Exception as e:

            return f"Calculation Error: {e}"

    def _evaluate(self, node):

        if isinstance(node, ast.Constant):

            return node.value

        if isinstance(node, ast.Num):

            return node.n

        if isinstance(node, ast.BinOp):

            left = self._evaluate(node.left)

            right = self._evaluate(node.right)

            op = OPERATORS[type(node.op)]

            return op(left, right)

        if isinstance(node, ast.UnaryOp):

            value = self._evaluate(node.operand)

            if isinstance(node.op, ast.USub):
                return -value

            if isinstance(node.op, ast.UAdd):
                return value

        raise ValueError("Unsupported Expression")