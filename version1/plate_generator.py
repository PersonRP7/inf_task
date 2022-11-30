import random

class PlateGenerator:

    # for i in PlateGenerator():
    #     data.append(f"{i}-{random.randint(0, 9)}")

    plates_int = []
    plates_str = []


    @classmethod
    def generate_plates(cls)->None:
        """
        Plate number creation.
        """
        cls.plates_int = random.sample(
            range(100, 500), 400
        )


    @classmethod
    def stringify_plates(cls)->None:
        """
        Stringify plate numbers to make them iterable.
        Iterability is needed for hyphen addition in the
        penultimate position of a given plate number.
        """
        for number in cls.plates_int:
            str(number)


    def __new__(cls) -> list:
        cls.generate_plates()
        return cls.plates



    