from Dinosaur import dinosaur

from Attack import attack

import random

class herd:
    def __init__(self):
        self.name = 'The Herd Before Time'

        self.t_rex = dinosaur('T. Rex', 200)
        self.stegosaurus = dinosaur('Stegosaurus', 120)
        self.spinosaurus = dinosaur('Spinosaurus', 150)
        self.dinos = [self.t_rex, self.stegosaurus, self.spinosaurus]

        self.bite = attack('Bite', 18)
        self.tail_sweep = attack('Tail Sweep', 10)
        self.attacks = [self.bite, self.tail_sweep]

    def attack(self):
        att = random.choice(self.attacks)
        return att