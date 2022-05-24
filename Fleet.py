from Robot import robot

from Weapon import weapon

class fleet:
    def __init__(self):
        self.name = 'League of Legends'

        self.optimus_prime = robot('Optimus Prime', 200)
        self.terminator = robot('The Terminator', 200)
        self.vision = robot('Vision', 180)
        
        self.ion_blaster = weapon('Ion Blaster', 20)
        self.energon_axe = weapon('Energon Axe', 15)
        self.energon_swords = weapon('Dual Energon Swords', 12)

        self.grenade_launcher = weapon('Grenade Launcher', 18)
        self.shotgun = weapon('Shotgon', 15)
        self.endo_battle_rifle = weapon('Endo Battle Rifle', 20)

        self.mjolnir = weapon('Mjolnir', 15)
        self.solar_beam = weapon('Solar Beam', 20)
        pass

    def check_fleet_health(self):
        fleet_health = int(self.optimus_prime.health) + int(self.terminator.health) + int(self.vision.health)
        return fleet_health

    def attack(self):
        ''
        pass



