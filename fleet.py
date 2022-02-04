from robot import Robot


class Fleet:

    def __init__(self):
        self.robot_list = []
        self.create_fleet()

    def create_fleet(self):
        robot_one = Robot('Bender')
        robot_two = Robot('Optimus')
        robot_three = Robot('Claptrap')
        self.robot_list.append(robot_one)
        self.robot_list.append(robot_two)
        self.robot_list.append(robot_three)


    


