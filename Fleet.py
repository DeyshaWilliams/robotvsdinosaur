from Robot import robot

from Weapon import weapon

class fleet:
    def __init__(self):
        self.optimus_prime = robot()
        self.terminator = robot()
        self.vision = robot()
        self.op_weapon_1 = weapon()
        self.op_weapon_2 = weapon()
        self.op_weapon_3 = weapon()
        self.term_weapon_1 = weapon()
        self.term_weapon_2 = weapon()
        self.term_weapon_3 = weapon()
        self.vis_weapon_1 = weapon()
        self.vis_weapon_2 = weapon()
        self.vis_weapon_3 = weapon()
        pass