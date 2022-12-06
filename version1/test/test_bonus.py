import sys

sys.path += ['./']
#Allows the tests to be run from the root directory, as python doesn't treat
#the current working directory as a package.

import unittest
from bonus import has_solution

#py -m unittest

class TestArithmetic(unittest.TestCase):

    def setUp(self) -> None:
        self.data = [ 
    "518-2, minus(plus(-5, -1), -8) = 2, 12",
    "000-4, root(root(0, 0!), 0!) = 1, 0"
    ]
        return super().setUp()

    def test_has_solution_returns_list_w_two_elements(self):
        self.assertEqual(len(has_solution(self.data)), 2)
    
