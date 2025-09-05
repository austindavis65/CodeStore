# # python -m unittest discover -vbs tests

import unittest

from squery03 import *
from lib import pencil

import random, os

class Test_query03(unittest.TestCase):

    def test_01(self):
        p = pencil.Pencil(pencil.MAX_NUM_LEADS)
        while p.get_num_leads() > 0 or p.get_current_lead_length() > 0:
            leads = p.get_num_leads()
            current = p.get_current_lead_length()

            correct_answer = leads * pencil.MAX_LEAD_LENGTH + current
            your_ans = query03(p)

            msg = "query03() returned total lead length %s." % (str(your_ans), )
            msg = msg + "  It should have returned a total lead length %s." % (str(correct_answer))
            msg = msg + "  Check your logic and try again."
            same = (your_ans == correct_answer)
            self.assertTrue(same, msg)

            p.click()

        return
