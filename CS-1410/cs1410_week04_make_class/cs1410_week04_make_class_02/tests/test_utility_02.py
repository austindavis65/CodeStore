# # python -m unittest discover -vbs tests

import unittest

from circle import *

class Test_CircleUtility02(unittest.TestCase):

    def test_01(self):
        c = Circle(3.14)
        correct_answer = 3.14
        your_ans = c.getRadius()

        msg = "getRadius() returned a radius of %s." % (str(your_ans), )
        msg = msg + "  It should have returned a radius of %s." % (str(correct_answer))
        msg = msg + "  Check your logic and try again."
        same = (abs(your_ans - correct_answer) < 0.0001)
        self.assertTrue(same, msg)


        radii   = [  1.0, 10.0,  100.0,  -1.0, 0.0 ]
        ret     = [ True, True,   True, False, True ]
        correct = [ 1.0, 10.0,  100.0, 100.0, 0.0 ]

        for i in range(len(correct)):

            # check return value
            correct_answer = ret[i]
            your_ans = c.setRadius(radii[i])

            msg = "setRadius(%s) returned %s." % (str(radii[i]), str(your_ans), )
            msg = msg + "  It should have returned %s." % (str(correct_answer))
            msg = msg + "  Check your logic and try again."
            same = (correct_answer == your_ans)
            self.assertTrue(same, msg)

            # check assigned radius
            correct_answer = correct[i]
            your_ans = c.getRadius()

            msg = "After setRadius(%s) the radius is %s." % (str(radii[i]), str(your_ans), )
            msg = msg + "  It should be %s." % (str(correct_answer))
            msg = msg + "  Check your logic and try again."
            same = (abs(your_ans - correct_answer) < 0.0001)
            self.assertTrue(same, msg)

            # check circumference
            correct_answer = correct[i] * 2.0 * 3.1415926535897
            your_ans = c.getCircumference()

            msg = "getCircumference() returned %s." % (str(your_ans), )
            msg = msg + "  It should be %s." % (str(correct_answer))
            msg = msg + "  Check your logic and try again."
            same = (abs(your_ans - correct_answer) < 0.0001)
            self.assertTrue(same, msg)

        return
