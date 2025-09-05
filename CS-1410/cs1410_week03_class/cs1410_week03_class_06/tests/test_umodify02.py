# # python -m unittest discover -vbs tests

import unittest

from umodify02 import *
from lib import pencil

import random, os

class Test_modify02(unittest.TestCase):

    def test_01(self):

        for i in range(pencil.MAX_NUM_LEADS +1):
            p = pencil.Pencil(i)
            p = modify02(p)

            correct_answer = i + 2
            if correct_answer > pencil.MAX_NUM_LEADS:
                correct_answer = pencil.MAX_NUM_LEADS

            your_ans = p.get_num_leads()

            msg = "modify02() returned a Pencil with %s leads." % (str(your_ans), )
            msg = msg + "  It should have returned a Pencil with %s leads." % (str(correct_answer))
            msg = msg + "  Check your logic and try again."
            same = (your_ans == correct_answer)
            self.assertTrue(same, msg)

        return
