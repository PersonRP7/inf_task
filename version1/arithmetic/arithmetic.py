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