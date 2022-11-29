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
        res = Arithmetic.addition(a, b)
        self.assertEqual(int(4), res)

    def test_subtraction_coerces_to_int(self):
        a = 10
        b = 5
        res = Arithmetic.subtraction(a, b)
        self.assertEqual(int(5), res)

    def test_multiplication_coerces_to_int(self):
        a = 10
        b = 5
        res = Arithmetic.multiplication(a, b)
        self.assertEqual(int(50), res)