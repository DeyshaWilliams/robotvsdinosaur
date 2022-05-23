from Dinosaur import dinosaur

from Attack import attack

class herd:
    def __init__(self):
        self.t_rex = dinosaur()
        self.stegosaurus = dinosaur()
        self.spinosaurus = dinosaur()
        self.t_attack = attack()
        self.steg_attack = attack()
        self.spin_attack_1 = attack()
        self.spin_attack_2 = attack()
        pass