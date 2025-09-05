# # python -m unittest discover -vbs tests

import unittest

from yquery01 import *
from lib import pencil

class Test_query01(unittest.TestCase):

    def test_01(self):

        correct_answers = [ 10, 9, 8, 7, 6, 5, 4, 3, 2, 1 ]

        p = pencil.Pencil(pencil.MAX_NUM_LEADS)

        for i in range(len(correct_answers)):
            correct_answer = correct_answers[i]
            your_ans = query01(p)

            msg = "query01() returned %s." % (str(your_ans), )
            msg = msg + "  It should have returned %s." % (str(correct_answer))
            msg = msg + "  Check your logic and try again."
            same = (your_ans == correct_answer)
            self.assertTrue(same, msg)

            p.click()

        return
