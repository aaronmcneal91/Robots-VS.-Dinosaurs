from ntpath import join
from dinosaur import Dinosaur

class Herd:

    def __init__(self):
        self.dino_list = []
        self.create_herd()
       
    def create_herd(self):
        dino_one = Dinosaur('Lil Tater', 25 )
        dino_two = Dinosaur('Milkshakes', 20)
        dino_three = Dinosaur('Clever Girl', 25)
        self.dino_list.append(dino_one)
        self.dino_list.append(dino_two)
        self.dino_list.append(dino_three)


        

       



