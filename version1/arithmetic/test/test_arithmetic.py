import sys

sys.path += ['./']
#Allows the tests to be run from the root directory, as python doesn't treat
#the current working directory as a package.

import unittest
from arithmetic import Arithmetic



#py -m unittest

class TestArithmetic(unittest.TestCase):

    def test_addition_coerces_to_int(self):
        a = 2
        b = 2
        res = Arithmetic.addition(2, 2)
        self.assertEqual(int(4), res)