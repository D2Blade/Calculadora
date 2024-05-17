class calc:
    def __init__(self, num1, op, num2):
        self.num1 = num1
        self.op = op
        self.num2 = num2
        

    def resultado(self):
        if self.op == 1:
            result = self.num1 + self.num2
        elif self.op == 2:
            result = self.num1 - self.num2
        elif self.op == 3:
            result = self.num1 * self.num2
        elif self.op == 4:
            result = self.num1 / self.num2
        print(f"Resultado: {result}")


conta = calc(float(input()),str(input()), float(input()))
if conta.op == '+':
    conta.op=1
elif conta.op == '-':
    conta.op=2
elif conta.op == '*':
    conta.op=3
elif conta.op == '/':
    conta.op=4

conta.resultado()
