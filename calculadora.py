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
            return f"Erro: Caractere não suportado"

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

def on_enter_key(event=None):
    expression = entry.get()
    calc = Calc(expression)
    result = calc.resultado()
    result_label.config(text=f"Resultado: {result}")


def show_placeholder(event, entry, placeholder):
    if entry.get() == '':
        entry.insert(0, placeholder)
        entry.config(fg='grey')

def hide_placeholder(event, entry, placeholder):
    if entry.get() == placeholder:
        entry.delete(0, tk.END)
        entry.config(fg='black')

#janela
root = tk.Tk()
root.title("Calculadora")
root.configure(bg='white')
root.geometry('300x80')
root.resizable(False,False)

#input
placeholder_text= "Insira a operação"
entry = tk.Entry(root,fg='gray',  width=40, highlightthickness=0, bd=0)
entry.pack(padx=10)
entry.insert(0, placeholder_text)
entry.bind('<FocusIn>', lambda event: hide_placeholder(event, entry, placeholder_text))
entry.bind('<FocusOut>', lambda event: show_placeholder(event, entry, placeholder_text))
entry.bind('<Return>', on_enter_key)

result_label = tk.Label(root, text='Resultado: ')
result_label.pack(pady=20)
result_label.configure(bg='white')

root.mainloop()

