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

    def check_herd_health(self):
        herd_health = self.t_rex.health + self.stegosaurus.health + self.spinosaurus.health
        return herd_health

    def attack():
        random.choice
