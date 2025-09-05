from mathproblem import MathProblem
class AdditionProblem:
    def __init__(self,lhs,rhs):
        self.lhs = lhs
        self.rhs = rhs
        math = MathProblem(lhs,rhs)
        math.setOperator('+')