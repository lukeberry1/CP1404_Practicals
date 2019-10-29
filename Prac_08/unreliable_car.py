
from Prac_08.car import Car
from random import randint

class Unreliable (Car):

    def __init__(self, name, fuel, reliability):
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        random_reliability = randint(1, 100)
        if random_reliability >= self.reliability:
            distance = 0
        return super().drive(distance)
