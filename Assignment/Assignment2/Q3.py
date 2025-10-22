class Stack:
    def __init__(self):
        self.items = []

    def push(self, x):
        self.items.append(x)

    def pop(self):
        return self.items.pop() if not self.isempty() else None

    def isempty(self):
        return len(self.items) == 0

    def display(self):
        print(self.items)

# RPN Evaluation
def evaluate_rpn(expr):
    stack = Stack()
    for char in expr:
        if char.isdigit():
            stack.push(int(char))
        else:
            b = stack.pop()
            a = stack.pop()
            if char == '+': stack.push(a + b)
            elif char == '-': stack.push(a - b)
            elif char == '*': stack.push(a * b)
            elif char == '/': stack.push(a / b)
    return stack.pop()

# Example
expr = "534*+"
print("RPN Result:", evaluate_rpn(expr))
