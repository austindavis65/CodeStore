# # python -m unittest discover -vbs tests

import unittest

from zcreate01 import *
from lib import pencil

class Test_create01(unittest.TestCase):

    def test_01(self):

        p = create01()
        correct_answer = 3
        your_ans = p.get_num_leads()

        msg = "create01() returned a Pencil with %s leads." % (str(your_ans), )
        msg = msg + "  It should have returned a Pencil with %s leads." % (str(correct_answer))
        msg = msg + "  Check your logic and try again."
        same = (your_ans == correct_answer)
        self.assertTrue(same, msg)

        correct_answer = pencil.MAX_LEAD_LENGTH
        your_ans = p.get_current_lead_length()

        msg = "create01() returned a Pencil with current lead length of %s." % (str(your_ans), )
        msg = msg + "  It should have returned a Pencil with current lead length of %s." % (str(correct_answer))
        msg = msg + "  Check your logic and try again."
        same = (your_ans == correct_answer)
        self.assertTrue(same, msg)

        return
