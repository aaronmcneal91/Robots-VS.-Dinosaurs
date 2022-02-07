
from lib2to3.pgen2.token import GREATEREQUAL
from random import Random
from fleet import Fleet
from herd import Herd

class Battlefield:

    def __init__(self):
        self.fleet = Fleet() 
        self.herd = Herd()     

    def run_game(self): 
        print('WELCOME TO PREHISTORIC FUTURISTIC HELL!!!')
        self.battle()


    
        
   
        
        
        
        

        
        
    
        
    def battle(self): 
        self.dino_turn()
        self.robo_turn()
        # while len in self.fleet.robot_list > 0:
        #     self.dino_turn()
        # while len in self.herd.dino_list > 0:
        #     self.dino_turn()
        # if len in self.fleet.robot_list < 0:
        #     self.display_winner()
        # if len in self.herd.dino_list < 0:
        #     self.display_winner()







        while len(self.fleet.robot_list) >= 0:
            self.dino_turn()
            self.robo_turn()
        if len(self.herd.dino_list) >= 0:
            self.dino_turn()
            self.robo_turn()
        else:
            self.display_winner()
        

        
        
            
        

       
       
       
       
       
       
       
       
       
       
        # self.dino_turn
       
        # while self.fleet.robot_list.len[0] >= 0:
        #     self.dino_turn
        # while self.herd.dino_list.len >= 0:
        #     self.dino_turn()
        # if self.fleet.robot_list <= len(0):
        #     self.display_winner()
        # if self.herd.dino_list <= len(0):
        #     self.display_winner
           


         



        
    def dino_turn(self): # I call this in battle(), how can we use the attack we tested here to get all dinos to attack robots
        print("It's the dino's turn!!" "Who would you like to attack with?")
        self.show_dino_options()
        user_dino_choice = int(input())
        print("select a robot to attack")
        self.show_robo_options()
        user_robot_choice = int(input())
        self.herd.dino_list[user_dino_choice].attack(self.fleet.robot_list[user_robot_choice])
        
        
         
    def robo_turn(self): 
        print("It's the Robot's turn!!" "Who would you like to attack with?")
        self.show_robo_options()
        user_robo_choice = int(input())
        print("select a dino to attack")
        self.show_dino_options()
        user_dino_choice = int(input())
        self.fleet.robot_list[user_robo_choice].attack(self.herd.dino_list[user_dino_choice])
        
        

        
    def show_dino_options(self):
        i = 0
        for dino in self.herd.dino_list:
            print(f'Press {i} to select {dino.name} ({dino.health} health remaining)')
            i += 1
            if dino.health <= 0:
                self.herd.dino_list.remove(dino)
            
        
    def show_robo_options(self):
        i = 0
        for robot in self.fleet.robot_list:
            print(f'Press {i} to select {robot.name} ({robot.health} health remaining)')
            i += 1
            if robot.health <= 0:
                self.fleet.robot_list.remove(robot)


    def display_winner(self):
        if self.herd.dino_list >= 0:
            print ('DINOS WIN!!')
        if self.fleet.robot_list >= 0:
            print('ROBOTS WIN!!')

    