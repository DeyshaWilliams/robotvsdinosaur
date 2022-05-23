from Dinosaur import dinosaur

from Attack import attack

class herd:
    def __init__(self):
        self.t_rex = dinosaur('T. Rex', 180)
        self.stegosaurus = dinosaur('Stegosaurus', 100)
        self.spinosaurus = dinosaur('Spinosaurus', 120)
        self.bite = attack('Bite', 15)
        self.tail_sweep = attack('Tail Sweep', 9)
        pass

    herd_health = ''