import unittest

from wcreate02 import *
from lib import pencil

class Test_create02(unittest.TestCase):

    def test_01(self):

        p = create02()
        correct_answer = pencil.MAX_NUM_LEADS
        your_ans = p.get_num_leads()

        msg = "create02() returned a Pencil with %s leads." % (str(your_ans), )
        msg = msg + "  It should have returned a Pencil with %s leads." % (str(correct_answer))
        msg = msg + "  Check your logic and try again."
        same = (your_ans == correct_answer)
        self.assertTrue(same, msg)

        correct_answer = pencil.MAX_LEAD_LENGTH
        your_ans = p.get_current_lead_length()

        msg = "create02() returned a Pencil with current lead length of %s." % (str(your_ans), )
        msg = msg + "  It should have returned a Pencil with current lead length of %s." % (str(correct_answer))
        msg = msg + "  Check your logic and try again."
        same = (your_ans == correct_answer)
        self.assertTrue(same, msg)

        return
