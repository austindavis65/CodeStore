# # python -m unittest discover -vbs tests

import unittest

from qmodify04 import *
from lib import pencil

import random, os

class Test_modify04(unittest.TestCase):

    def test_01(self):
        for i in range(pencil.MAX_NUM_LEADS, 0, -1):
            p = pencil.Pencil(i)
            for j in range(0, i):
                p.click()
            p = modify04(p)

            correct_answer = i - 1
            your_ans = p.get_num_leads()

            msg = "modify04() returned a Pencil with %s leads." % (str(your_ans), )
            msg = msg + "  It should have returned a Pencil with %s leads." % (str(correct_answer))
            msg = msg + "  Check your logic and try again."
            same = (your_ans == correct_answer)
            self.assertTrue(same, msg)

            correct_answer = pencil.MAX_LEAD_LENGTH
            your_ans = p.get_current_lead_length()

            msg = "modify04() returned a Pencil with current lead length of %s." % (str(your_ans), )
            msg = msg + "  It should have returned a Pencil with current lead length of %s." % (str(correct_answer))
            msg = msg + "  Check your logic and try again."
            same = (your_ans == correct_answer)
            self.assertTrue(same, msg)

        return
