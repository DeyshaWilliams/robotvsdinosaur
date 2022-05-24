from Robot import robot

from Weapon import weapon

class fleet:
    def __init__(self):
        self.name = 'League of Legends'

        self.optimus_prime = robot('Optimus Prime', 200)
        self.terminator = robot('The Terminator', 200)
        self.vision = robot('Vision', 180)
        self.robots = [self.optimus_prime, self.terminator, self.vision]
        
        self.op_weapon_1 = weapon('Ion Blaster', 20)
        self.op_weapon_2 = weapon('Energon Axe', 15)
        self.op_weapon_3 = weapon('Dual Energon Swords', 12)

        self.term_weapon_1 = weapon('Grenade Launcher', 18)
        self.term_weapon_2 = weapon('Shotgon', 15)
        self.term_weapon_3 = weapon('Endo Battle Rifle', 20)

        self.vis_weapon_1 = weapon('Mjolnir', 15)
        self.vis_weapon_2 = weapon('Solar Beam', 20)
        pass

    def check_fleet_health(self):
        fleet_health = 0
        for robot in self.robots:
            fleet_health += robot.health
        pass




