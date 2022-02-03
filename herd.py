from ntpath import join
from dinosaur import Dinosaur

dino1 = Dinosaur('Lil Tator',30 )



class Herd:

    def __init__(self):
        self.dinosaurs = [dino1]
        print(dino1.name) 
        print('Attack Power:', dino1.attack_power, 'Health:', dino1.health)
        
        

        

    def create_herd(self):
        print(self.dinosaurs)



