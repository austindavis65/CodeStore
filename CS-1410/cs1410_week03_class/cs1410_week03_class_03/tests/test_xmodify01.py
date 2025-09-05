# # python -m unittest discover -vbs tests

import unittest

from xmodify01 import *
from lib import pencil

def total_lead(p):
    leads = p.get_num_leads()
    current = p.get_current_lead_length()
    return leads * pencil.MAX_LEAD_LENGTH + current

class Test_modify01(unittest.TestCase):

    def test_01(self):

        p = pencil.Pencil(pencil.MAX_NUM_LEADS)
        value = total_lead(p)
        while total_lead(p) >= 13:
            p = modify01(p)
            value -= 13

            correct_answer = value
            your_ans = total_lead(p)

            msg = "modify01() returned a Pencil with %s total lead length." % (str(your_ans), )
            msg = msg + "  It should have returned a Pencil with %s total lead length." % (str(correct_answer))
            msg = msg + "  Check your logic and try again."
            same = (your_ans == correct_answer)
            self.assertTrue(same, msg)

        return
