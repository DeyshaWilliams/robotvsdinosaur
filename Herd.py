from Dinosaur import dinosaur

from Attack import attack

import random

class herd:
    def __init__(self):
        self.name = 'The Herd Before Time'

        self.t_rex = dinosaur('T. Rex', 180)
        self.stegosaurus = dinosaur('Stegosaurus', 100)
        self.spinosaurus = dinosaur('Spinosaurus', 120)
        self.dinos = [self.t_rex, self.stegosaurus, self.spinosaurus]

        self.bite = attack('Bite', 15)
        self.tail_sweep = attack('Tail Sweep', 9)
        self.attacks = [self.bite, self.tail_sweep]
        pass

    

    def herd_health(self):
        herd_health = 0
        for dino in self.dinos:
            herd_health += int(dino.health)
        return herd_health

    def attack(self):
        att = random.choice(self.attacks)
        return att