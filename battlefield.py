from Fleet import fleet

from Herd import herd

import random

class battlefield:
    def __init__(self, name):
        self.name = name
        self.fleet = fleet()
        self.herd = herd()
        self.act_fleet_health = 0
        pass


    def run_game(self):
        print('Game: Start!')
        self.greeting()
        self.game()
        
    def game(self):
        is_dead = False
        herd_health = self.herd.herd_health()

        while is_dead == False:
            self.act_fleet_health = self.check_fleet_health()

            if self.act_fleet_health <= 0 or herd_health <= 0:
                is_dead = True
            if self.act_fleet_health <= 0:
                print(f'{self.fleet.name} defeated {self.herd.name}!')
            elif herd_health <= 0:
                print(f'{self.herd.name} defeated {self.fleet.name}')
            if is_dead == True:
                self.ending()    

    def greeting(self):
        print(
            f'''
***********

***********            
            '''
        )
    
    def herd_dealt_dmg(self):
        chrg_dino = random.choice(self.herd.dinos)
        hurt_robot = random.choice(self.fleet.robots)
        att = self.herd.attack()
        print(f'{chrg_dino.name} dealt {att.dmg} damage to {hurt_robot.name}')
        return att.dmg

    def check_fleet_health(self):
        fleet_health = self.fleet_health(self.act_fleet_health)
        dmg_done = self.herd_dealt_dmg()
        fleet_health -= dmg_done
        return fleet_health

    def fleet_health(self, health_passed):
        fleet_health = int(health_passed)
        if fleet_health > 0:
            return fleet_health
        else:
            for robo in self.fleet.robots:
                fleet_health += int(robo.health)
        return fleet_health
 
    def ending(self):
        print('Thank you and good night!')
 
