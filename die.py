from random import randint

class Die:
    """Class to represent die"""

    def __init__(self, num_sides=6):
        """Assume a 6 sided dice"""
        self.num_sides = num_sides

    def roll(self):
        return randint(1, self.num_sides)