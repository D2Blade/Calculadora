import ast
import operator as op

operators = {
    ast.Add: op.add,
    ast.Sub: op.sub,
    ast.Mult: op.mul,
    ast.Div: op.truediv,
    ast.Pow: op.pow,
    ast.BitXor: op.xor,
}

class Calc:
    def __init__(self, expression):
        self.expression = expression

    def eval_expr(self, expr):
        try:

            node = ast.parse(expr, mode='eval').body
            return self._eval(node)
        except Exception as e:
            print(f"Erro: {e}")
            return None

    def _eval(self, node):
        if isinstance(node, ast.BinOp):
            left = self._eval(node.left)
            right = self._eval(node.right)
            operator_func = operators[type(node.op)]
            return operator_func(left, right)
        elif isinstance(node, ast.Num):
            return node.n
        else:
            raise TypeError(node)

    def resultado(self):
        result = self.eval_expr(self.expression)
        if result is not None:
            print(f"Resultado: {result}")

expression = input("Digite a expressão matemática: ")
conta = Calc(expression)
conta.resultado()
