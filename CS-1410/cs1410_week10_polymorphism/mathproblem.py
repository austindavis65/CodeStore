class MathProblem:
    def __init__(self,lhs,rhs):
        self.lhs = lhs
        self.rhs = rhs
        self.operator = ""

    def getLHS(self):
        return self.lhs

    def getRHS(self):
        return self.rhs

    def getOperator(self):
        return self.operator

    def setOperator(self,string):
        self.operator = string
        return True

    def setLHS(self,value):
        if value != self.lhs:
            self.lhs = value
            return True
        else:
            return False

    def setRHS(self,value):
        if value != self.rhs:
            self.rhs = value
            return True
        else:
            return False

    def getString(self):
        return ''

    def checkAnswer(self,ans):
        return False
