from mimetypes import init
import numbers


import random

class PlateGenerator:

    plates = []


    @classmethod
    def generate_plates(cls)->None:
        cls.plates = random.sample(
            range(1000, 5000), 3000
        )

    @classmethod
    def stringify_plates(cls)->None:
        for number in cls.plates:
            str(number)


    def __new__(cls) -> list:
        cls.generate_plates()
        cls.stringify_plates()
        return cls.plates



    