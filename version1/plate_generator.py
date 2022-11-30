import random

class PlateGenerator:

    """
    Uses __new__ to return a list of plate numbers
    in the designated format (nnn-n) upon instantiation,
    ie. PlateGenerator()
    """

    plates_int = []
    plates_str = []


    @classmethod
    def generate_plates(cls)->None:
        """
        3 digit plate root creation. Not used by itself.
        Used by stringify_plates.
        """
        cls.plates_int = random.sample(
            range(100, 500), 400
        )

    @classmethod
    def stringify_plates(cls)->None:
        """
        Populates the plates_str list with the 3 digit plates
        suffixed by '-n' where n -> [0, 9].
        """
        cls.generate_plates()
        for plate in cls.plates_int:
            cls.plates_str.append(f"{plate}-{random.randint(0, 9)}")


    def __new__(cls) -> list:
        cls.stringify_plates()
        return cls.plates_str



    