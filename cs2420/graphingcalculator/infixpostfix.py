from stack import Stack


def PrintDirections():
    print('Write a mathmatical expression using single digit numbers and the operators: +, -, /, *, ^', '\n', 'Parentheis may be used ()', '\n' , "('^' is used for exponents)")


def InfixToPostfix(infix):
    postfix=""
    s = Stack()
    for c in infix:
        if c in '0123456789x':
            postfix += c
        if c in '+-':
            # while not s.IsEmpty() and s.Top() in '+-*/':
            while not s.IsEmpty() and s.Top() in '^+-*/':
                postfix+=s.pop()
            s.Push(c)

        if c in '*/':
            # while not s.IsEmpty() and s.Top() in '*/':
            while not s.IsEmpty() and s.Top() in '^*/':
                postfix+=s.pop()
            s.Push(c)

        if c in '^':
            # while not s.IsEmpty() and s.Top() in '^+-*/':
            while not s.IsEmpty() and s.Top() in '^':
                postfix+=s.pop()
            s.Push(c)

        if c == '(':
            s.Push(c)

        if c == ')':
            while s.Top() != '(':
                postfix+=s.pop()
            s.pop()

    while not s.IsEmpty():
        postfix += s.pop()

    return postfix



def EvaluatePostfix(postfix, x):
    s = Stack()
    for c in postfix:
        if c in '0123456789':
            s.Push(float(c))
        if c == 'x':
            s.Push(x)
        if c == '+':
            R = s.pop()
            L = s.pop()
            s.Push(L+R)
        if c == '-':
            R = s.pop()
            L = s.pop()
            s.Push(L-R)
        if c == '/':
            R = s.pop()
            L = s.pop()
            s.Push(L/R)
        if c == '*':
            R = s.pop()
            L = s.pop()
            s.Push(L*R)
        if c == '^':
            R = s.pop()
            L = s.pop()
            s.Push(L**R)

    return s.Top()


