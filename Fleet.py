
from Robot import robot

from Weapon import weapon

import random

class fleet:
    def __init__(self):
        self.name = 'League of Legends'

        self.optimus_prime = robot('Optimus Prime', 200)
        self.terminator = robot('The Terminator', 200)
        self.vision = robot('Vision', 180)
        self.robots = [self.optimus_prime, self.terminator, self.vision]
        
        self.ion_blaster = weapon('Ion Blaster', 20)
        self.energon_axe = weapon('Energon Axe', 15)
        self.energon_swords = weapon('Dual Energon Swords', 12)
        self.op_weapons = [self.ion_blaster, self.energon_axe, self.energon_swords]

        self.grenade_launcher = weapon('Grenade Launcher', 18)
        self.shotgun = weapon('Shotgon', 15)
        self.endo_battle_rifle = weapon('Endo Battle Rifle', 20)
        self.term_weapons = [self.grenade_launcher, self.endo_battle_rifle, self.shotgun]

        self.mjolnir = weapon('Mjolnir', 15)
        self.solar_beam = weapon('Solar Beam', 20)
        self.vis_weapons = [self.mjolnir, self.solar_beam]

    def op_attack(self):
        att = random.choice(self.op_weapons)
        return att
    
    def term_attack(self):
        att = random.choice(self.term_weapons)
        return att
    
    def vis_attack(self):
        att = random.choice(self.vis_weapons)
        return att
