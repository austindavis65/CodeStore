# # python -m unittest discover -vbs tests

import unittest, math

from blob import Blob, KIND_FOOD, KIND_PLAYER, KIND_AI

class Test_BlobMovement(unittest.TestCase):

    def test_01(self):
        s     = 1.0/math.sqrt(2.0)
        d     = 100.
        w_width = 500
        w_height = 400
        data = [ ( d,  0,  1,  0),
                 ( d,  d,  s,  s),
                 ( 0,  d,  0,  1),
                 (-d,  d, -s,  s),
                 (-d,  0, -1,  0),
                 (-d, -d, -s, -s),
                 ( 0, -d,  0, -1),
                 ( d, -d,  s, -s), ]

        # radius 5
        b1 = Blob(math.pi, 250., 200., w_width, w_height, KIND_AI)

        for x, y, dx, dy in data:
            bx = b1.getX()
            by = b1.getY()
            position = (b1.getX()+x, b1.getY()+y)
            b1 <<= position
            amount = 1.0
            b1 >>= amount

            self.assertAlmostEqual(bx + dx*amount, b1.getX(), places=4)
            self.assertAlmostEqual(by + dy*amount, b1.getY(), places=4)

        b1 <<= (-w_width, b1.getY())
        b1 >>= w_width
        r = b1.getRadius()
        self.assertAlmostEqual(r, b1.getX(), places=4, msg="What should " \
                "happen if the blob tries to go off the left of the screen?")

        b1 <<= (b1.getX(), -w_height)
        b1 >>= w_height
        self.assertAlmostEqual(r, b1.getY(), places=4, msg="What should " \
                "happen if the blob tries to go off the top of the screen?")

        b1 <<= (2*w_width, b1.getY())
        b1 >>= 2*w_width
        r = b1.getRadius()
        self.assertAlmostEqual(w_width-r, b1.getX(), places=4, msg="What " \
                "should happen if the blob tries to go off the right of the " \
                "screen?")

        b1 <<= (b1.getX(), 2*w_height)
        b1 >>= 2*w_height
        self.assertAlmostEqual(w_height-r, b1.getY(), places=4, msg="What " \
                "should happen if the blob tries to go off the bottom of " \
                "the screen?")

        return
