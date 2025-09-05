# # python -m unittest discover -vbs tests

import unittest

from rmodify03 import *
from lib import pencil

import random, os

class Test_modify03(unittest.TestCase):

    def test_01(self):
        p = pencil.Pencil(pencil.MAX_NUM_LEADS)
        p = modify03(p)

        correct_answer = 1
        your_ans = p.get_num_leads()

        msg = "modify03() returned a Pencil with %s leads." % (str(your_ans), )
        msg = msg + "  It should have returned a Pencil with %s leads." % (str(correct_answer))
        msg = msg + "  Check your logic and try again."
        same = (your_ans == correct_answer)
        self.assertTrue(same, msg)


        correct_answer = 4
        your_ans = p.get_current_lead_length()

        msg = "modify04() returned a Pencil with current lead length of %s." % (str(your_ans), )
        msg = msg + "  It should have returned a Pencil with current lead length of %s." % (str(correct_answer))
        msg = msg + "  Check your logic and try again."
        same = (your_ans == correct_answer)
        self.assertTrue(same, msg)

        return
