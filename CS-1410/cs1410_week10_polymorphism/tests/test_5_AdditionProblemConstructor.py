# # python -m unittest discover -vbs tests

import unittest

from additionproblem import AdditionProblem

class Test_AdditionProblemConstructor(unittest.TestCase):

    def test_01(self):
        values = [ (-10, -10), (10, -10), (10, 10), (-10, 10), (10, 10),  ]
        for lhs, rhs in values:
            s = AdditionProblem(lhs, rhs)
            self.assertEqual(lhs, s.getLHS())
            self.assertEqual(rhs, s.getRHS())
            self.assertEqual("+", s.getOperator())
        return
