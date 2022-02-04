from weapon import Weapon


class Robot:

    def __init__(self, name):
        self.name = name
        self.health = 100
        self.weapon = Weapon('lightsaber', 25)

    def attack(self,dinosaur):
        dinosaur.health -= self.weapon.attack_power
        print(f'{self.name} is attacking {dinosaur.name} using {self.weapon.name} doing {self.weapon.attack_power} damage')
        print(f'{dinosaur.name} has {dinosaur.health} remaining health')
    