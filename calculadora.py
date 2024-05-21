import tkinter as tk
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
            return f"Erro: {e}"

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
        return self.eval_expr(self.expression)

def on_button_click():
    expression = entry.get()
    calc = Calc(expression)
    result = calc.resultado()
    result_label.config(text=f"Resultado: {result}")

root = tk.Tk()
root.title("Calculadora de Expressões")

entry = tk.Entry(root, width=40)
entry.pack(pady=10)

button = tk.Button(root, text="Calcular", command=on_button_click)
button.pack(pady=10)

result_label = tk.Label(root, text="Resultado: ")
result_label.pack(pady=10)

root.mainloop()

