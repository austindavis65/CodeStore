from graphics import *

class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

def infix_to_postfix(expression):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
    output = ''
    operator_stack = Stack()

    for char in expression:
        if char.isdigit() or char == 'x':
            output += char
        elif char == '(':
            operator_stack.push(char)
        elif char == ')':
            while not operator_stack.is_empty() and operator_stack.peek() != '(':
                output += operator_stack.pop()
            operator_stack.pop()
        else:
            while not operator_stack.is_empty() and precedence.get(operator_stack.peek(), 0) >= precedence.get(char, 0):
                output += operator_stack.pop()
            operator_stack.push(char)

    while not operator_stack.is_empty():
        output += operator_stack.pop()

    return output

def evaluate_postfix(expression, x):
    stack = Stack()

    for char in expression:
        if char.isdigit():
            stack.push(int(char))
        elif char == 'x':
            stack.push(x)
        else:
            operand2 = stack.pop()
            operand1 = stack.pop()
            result = 0
            if char == '+':
                result = operand1 + operand2
            elif char == '-':
                result = operand1 - operand2
            elif char == '*':
                result = operand1 * operand2
            elif char == '/':
                result = operand1 / operand2
            stack.push(result)

    return stack.pop()

def plot_graph(expression):
    win = GraphWin("Graphing Calculator", 600, 600)
    win.setBackground("white")
    win.setCoords(-10, -10, 10, 10)

    polyline = []
    for x in range(-100, 101):
        y = evaluate_postfix(expression, x/10)
        polyline.append(Point(x/10, y))

    graph = Polygon(*polyline)
    graph.setWidth(2)
    graph.draw(win)

    Text(Point(0, -9.5), "Click anywhere to close the window").draw(win)
    win.getMouse()
    win.close()

def main():
    expression = input("Enter a mathematical expression (use 'x' as the variable): ")
    postfix_expression = infix_to_postfix(expression)
    print("Postfix expression:", postfix_expression)
    plot_graph(postfix_expression)

if __name__ == "__main__":
    main()
