from robot import Robot
robo1 = Robot('Claptrap')

class Fleet:

    def __init__(self):
        self.robots = [robo1]
        print(robo1.name) 
        print('Lightsaber Power:25', robo1.health, 'Health:', robo1.health)

    def create_fleet(self):
       print(self.robots)


