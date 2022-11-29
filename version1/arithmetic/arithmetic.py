from math import factorial
from itertools import product

class Arithmetic:

    @staticmethod
    def addition(a:int, b:int)->int:
        return int(a) + int(b)

    @staticmethod
    def subtraction(a:int, b:int)->int:
        return int(a) - int(b)

    @staticmethod
    def multiplication(a:int, b:int)->int:
        return int(a) * int(b)

    @staticmethod
    def division(a:int, b:int)->int:
        return int(a) / int(b)

    @staticmethod
    def factorial(a:int)->int:
        return factorial(int(a))

    @staticmethod
    def power_to(a:int, b:int)->int:
        return int(a**b)

    @staticmethod
    def root(a:int, b:int)->int:
        # root(4, 625)
        # return a**(1 / b)
        return int(b**(1 / a))