import sys
import numpy as np
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLineEdit
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from stack import Stack

class Calculator(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Graphing Calculator")
        self.setGeometry(100, 100, 800, 600)

        self.layout = QVBoxLayout()
        self.expression_input = QLineEdit()
        self.layout.addWidget(self.expression_input)

        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        self.layout.addWidget(self.canvas)

        self.setLayout(self.layout)

        self.expression_input.textChanged.connect(self.update_graph)

    def update_graph(self):
        expression = self.expression_input.text()
        if expression:
            x = np.linspace(-10, 10, 400)
            y = self.evaluate_expression(expression, x)
            self.plot_graph(x, y)

    def evaluate_expression(self, expression, x):
        postfix = self.infix_to_postfix(expression)
        y = []
        for val in x:
            y.append(self.evaluate_postfix(postfix, val))
        return y

    def infix_to_postfix(self, infix):
        postfix = ""
        s = Stack()
        for c in infix:
            if c in '0123456789x':
                postfix += c
            if c in '+-':
                while not s.IsEmpty() and s.Top() in '^+-*/':
                    postfix += s.pop()
                s.Push(c)
            if c in '*/':
                while not s.IsEmpty() and s.Top() in '^*/':
                    postfix += s.pop()
                s.Push(c)
            if c in '^':
                while not s.IsEmpty() and s.Top() in '^':
                    postfix += s.pop()
                s.Push(c)
            if c == '(':
                s.Push(c)
            if c == ')':
                while s.Top() != '(':
                    postfix += s.pop()
                s.pop()
        while not s.IsEmpty():
            postfix += s.pop()
        return postfix

    def evaluate_postfix(self, postfix, x):
        s = Stack()
        for c in postfix:
            if c in '0123456789':
                s.Push(float(c))
            if c == 'x':
                s.Push(x)
            if c == '+':
                R = s.pop()
                L = s.pop()
                s.Push(L + R)
            if c == '-':
                R = s.pop()
                L = s.pop()
                s.Push(L - R)
            if c == '/':
                R = s.pop()
                L = s.pop()
                s.Push(L / R)
            if c == '*':
                R = s.pop()
                L = s.pop()
                s.Push(L * R)
            if c == '^':
                R = s.pop()
                L = s.pop()
                s.Push(L ** R)
        return s.Top()

    def plot_graph(self, x, y):
        self.figure.clear()
        ax = self.figure.add_subplot(111)
        ax.plot(x, y)
        ax.grid(True)
        self.canvas.draw()

def main():
    app = QApplication(sys.argv)
    window = QMainWindow()
    calculator = Calculator()
    window.setCentralWidget(calculator)
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()