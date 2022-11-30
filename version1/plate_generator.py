import random

class PlateGenerator:

    plates = []


    @classmethod
    def generate_plates(cls)->None:
        """
        Plate number creation.
        """
        cls.plates = random.sample(
            range(1000, 5000), 3000
        )

    @classmethod
    def stringify_plates(cls)->None:
        """
        Stringify plate numbers to make them iterable.
        Iterability is needed for hyphen addition in the
        penultimate position of a given plate number.
        """
        for number in cls.plates:
            str(number)


    def __new__(cls) -> list:
        cls.generate_plates()
        cls.stringify_plates()
        return cls.plates



    