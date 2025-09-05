# # python -m unittest discover -vbs tests

import unittest

from vquery02 import *
from lib import pencil

import random, os

class Test_query02(unittest.TestCase):

    def test_01(self):

        p = pencil.Pencil(pencil.MAX_NUM_LEADS)

        while p.get_num_leads() > 0:
            correct_answer = p.get_num_leads()
            your_ans = query02(p)

            msg = "query02() returned %s." % (str(your_ans), )
            msg = msg + "  It should have returned %s." % (str(correct_answer))
            msg = msg + "  Check your logic and try again."
            same = (your_ans == correct_answer)
            self.assertTrue(same, msg)

            while p.get_num_leads() == correct_answer:
                p.click()

        return
