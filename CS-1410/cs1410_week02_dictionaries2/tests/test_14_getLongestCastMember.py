# # python -m unittest discover -vbs tests

import unittest

from monsterfunctions import *

import random, math

class Test_get_longest_cast_member(unittest.TestCase):

    def test_01(self):
        data = [ ("Mike",                      "Billy Crystal"),
                 ("Sully",                     "John Goodman"),
                 ("Johnny Worthington III",    "Nathan Fillion"),
                 ("Dean Abigail Hardscrabble", "H. Mirren"),
        ]
        tests = [ "Billy Crystal", "Billy Crystal", "Nathan Fillion", "Nathan Fillion" ]

        monsters = create_monster_cast()

        for i in range(len(data)):
            monsters = add_cast_member(monsters, data[i][0], data[i][1])
            your_answer = get_longest_cast_member(monsters)
            self.assertEqual(tests[i], your_answer)

        return
