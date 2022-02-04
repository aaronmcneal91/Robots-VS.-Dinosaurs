from random import Random
from fleet import Fleet
from herd import Herd

class Battlefield:

    def __init__(self):
        self.fleet = Fleet()  #  TESTED
        self.herd = Herd()     # TESTED

    def run_game(self): 

        print("It's the dino's turn!!" "Who would you like to attack?")

        
        self.show_robo_opponent_options()
        victim = input('')
        if victim == '0':
            self.herd.dino_list[0].attack(self.fleet.robot_list[0])
        

        # if victim == '1':
        #     self.herd.dino_list[0].attack(self.fleet.robot_list[1])
        # if victim == '2':
        #     self.herd.dino_list[0].attack(self.fleet.robot_list[3])
        
               

        print("It's the robot's turn!!" "Who would you like to attack?")
        
        self.show_dino_opponent_options()
        victim = input('')
        if victim =='0':
            self.fleet.robot_list[0].attack(self.herd.dino_list[0])

        while self.fleet.robot_list == '0':
            self.run_game 
        while self.herd.dino_list == '0':
            self.run_game


            
        
        # if victim == '1':
        #     self.fleet.robot_list[0].attack(self.herd.dino_list[1])
        # if victim == '2':
        #     self.fleet.robot_list[0].attack(self.herd.dino_list[2])
        
        
    
  
    
    # def display_welcome(self):
        pass
    def battle(self): # while dino and robot list are greater than 0 it just continues to loop over dino_turn and robot_turn
        

        pass
    def dino_turn(self, dinosaur): # I call this in battle(), how can we use the attack we tested here to get all dinos to attack robots
        # print("It's the dino's turn!!")
        # self.herd.dino_list[0].attack(self.fleet.robot_list[0])
        # self.show_robo_opponent_options()
        
         pass
    def robo_turn(self, robot): # same as dino turn
        # print("It's the robot's turn!!")
        # self.fleet.robot_list[0].attack(self.herd.dino_list[0]) 
        # self.show_dino_opponent_options()

        pass
    def show_dino_opponent_options(self): # I use this to just print the options avaialble to the user
        i = 0
        for dino in self.herd.dino_list:
            print(f'Press {i} to select {dino.name} ({dino.health} health remaining')
            i += 1
            if dino.health >= 0:
                self.herd.dino_list.remove
        pass
    def show_robo_opponent_options(self):
        i = 0
        for robot in self.fleet.robot_list:
            print(f'Press {i} to select {robot.name} ({robot.health} health remaining)')
            i += 1
            if robot.health >= 0:
                self.fleet.robot_list.remove

        # pass
    def display_winner(self):
        if self.herd.dino_list >= 0:
            print ('DINOS WIN!!')
        if self.fleet.robot_list >= 0:
            print('ROBOTS WIN!!')

    