# # python -m unittest discover -vbs tests

import unittest

from tcreate03 import *
from lib import pencil

import random, os

class Test_create03(unittest.TestCase):

    def test_01(self):
        init_leads      = [ 0, 1, 2, 3, 4, 5, 6, 7 ]
        correct_answers = [ 0, 1, 2, 3, 4, 5, 5, 5 ]

        for i in range(len(init_leads)):
            p = create03(init_leads[i])
            correct_answer = correct_answers[i]
            your_ans = p.get_num_leads()

            msg = "create03(%s) returned a Pencil with %s leads." % (str(init_leads[i]), str(your_ans), )
            msg = msg + "  It should have returned a Pencil with %s leads." % (str(correct_answer))
            msg = msg + "  Check your logic and try again."
            same = (your_ans == correct_answer)
            self.assertTrue(same, msg)

        return
