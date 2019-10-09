from prac_08.car import Car
import random


class UnreliableCar(Car):
    reliability = 50

    def __init__(self, name, fuel):
        super().__init__(name, fuel)

    def drive(self, distance):
        if random.randint(0, 100) < self.reliability:
            super().drive(distance)
        return distance
