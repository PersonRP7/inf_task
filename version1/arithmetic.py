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

    @staticmethod
    def inverter(data:list)->list:
        # data = [5, 3, 3]
        """
        Creates a cartesian product of all possible sign variations
        for every digit in a three digit list comprising a given registration
        number.
        """
        inverted_data = [-x for x in data]
        res = list(product(*zip(data, inverted_data)))
        # print(res)
        return res