# # python -m unittest discover -vbs tests

import unittest

from shape import Shape
from circle import Circle
from rectangle import Rectangle
from square import Square

class Test_MoveMethod(unittest.TestCase):

    def test_01(self):
        x = 13
        y = 17
        w = 19
        h = 23
        r = 29
        s = 31

        shp = Shape(x, y)
        crc = Circle(x, y, r)
        rct = Rectangle(x, y, w, h)
        sqr = Square(x, y, s)

        moves      = [ (-1, 1), (1, -1), (-1, -1), (1, 1),
                       (-1, 0), (0, -1), (1, 0), (0, 1),
                       (0, 0) ]

        for dx,dy in moves:
            for sp in [ shp, crc, rct, sqr ]:
                self.assertEqual(x, sp.getX())
                self.assertEqual(y, sp.getY())

                if dx or dy:
                    self.assertEqual(True, sp.move(dx, dy))
                else:
                    self.assertEqual(False, sp.move(dx, dy))

                self.assertEqual(x + dx, sp.getX())
                self.assertEqual(y + dy, sp.getY())

            x += dx
            y += dy

        return
