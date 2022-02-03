from weapon import Weapon


class Robot:

    def __init__(self, name):
        self.name = name
        self.health = 100
        self.weapon = Weapon('lightsaber', 25)

    def attack(self,dinosaur):
        self.attack = 25
    