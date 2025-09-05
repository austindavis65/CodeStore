# # python -m unittest discover -vbs tests

import unittest

from car import *

class Test_CarUtility02(unittest.TestCase):

    def test_01(self):
        brake   = [ 0.1,   1.0, 2.3,  12.3,   0.0,   -1.0, 100.0,   1.0 ]
        ret     = [ True, True, True, True, False, False,  True, False ]
        correct = [ 59.9, 58.9, 56.6, 44.3,  44.3,  44.3,   0.0,   0.0 ]

        # check initial speed
        c = Car()
        correct_answer = 0.0
        your_ans = c.getSpeed()

        msg = "getSpeed() returned a speed of %s." % (str(your_ans), )
        msg = msg + "  It should have returned a speed of %s." % (str(correct_answer))
        msg = msg + "  Check your logic and try again."
        same = (abs(your_ans - correct_answer) < 0.0001)
        self.assertTrue(same, msg)

        # give car speed so that brake() makes sense
        correct_answer = True
        your_ans = c.setSpeed(60.0)

        msg = "setSpeed(%s) returned %s." % (str(60.0), str(your_ans), )
        msg = msg + "  It should have returned %s." % (str(correct_answer))
        msg = msg + "  Check your logic and try again."
        same = (correct_answer == your_ans)
        self.assertTrue(same, msg)


        # check assigned speed
        correct_answer = 60.0
        your_ans = c.getSpeed()

        msg = "After setSpeed(%s) the speed is %s." % (str(60.0), str(your_ans), )
        msg = msg + "  It should be %s." % (str(correct_answer))
        msg = msg + "  Check your logic and try again."
        same = (abs(your_ans - correct_answer) < 0.0001)
        self.assertTrue(same, msg)

        # finally, test brake()
        for i in range(len(correct)):
            # check return value
            correct_answer = ret[i]
            your_ans = c.brake(brake[i])

            msg = "brake(%s) returned %s." % (str(brake[i]), str(your_ans), )
            msg = msg + "  It should have returned %s." % (str(correct_answer))
            msg = msg + "  Check your logic and try again."
            same = (correct_answer == your_ans)
            self.assertTrue(same, msg)

            # check assigned speed
            correct_answer = correct[i]
            your_ans = c.getSpeed()

            msg = "After brake(%s) the speed is %s." % (str(brake[i]), str(your_ans), )
            msg = msg + "  It should be %s." % (str(correct_answer))
            msg = msg + "  Check your logic and try again."
            same = (abs(your_ans - correct_answer) < 0.0001)
            self.assertTrue(same, msg)

        return
