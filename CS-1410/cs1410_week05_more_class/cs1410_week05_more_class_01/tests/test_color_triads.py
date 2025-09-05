# # python -m unittest discover -vbs tests

import unittest

from color import *

class Test_ColorTriad(unittest.TestCase):

    def test_01(self):
        reds    = [ 0, 100, 200, 255 ]
        greens  = [ 0, 100, 200, 255 ]
        blues   = [ 0, 100, 200, 255 ]

        for red in reds:
            for green in greens:
                for blue in blues:
                    c = Color(red, green, blue)
                    self.assertEqual(c.getRed(), red)
                    self.assertEqual(c.getGreen(), green)
                    self.assertEqual(c.getBlue(), blue)
                    c.triad()
                    self.assertEqual(c.getRed(), green)
                    self.assertEqual(c.getGreen(), blue)
                    self.assertEqual(c.getBlue(), red)
                    c.triad()
                    self.assertEqual(c.getRed(), blue)
                    self.assertEqual(c.getGreen(), red)
                    self.assertEqual(c.getBlue(), green)
                    c.triad()
                    self.assertEqual(c.getRed(), red)
                    self.assertEqual(c.getGreen(), green)
                    self.assertEqual(c.getBlue(), blue)
        return
