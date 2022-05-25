
from Fleet import fleet

from Herd import herd

import random

class battlefield:
    def __init__(self, name):
        self.name = name
        self.fleet = fleet()
        self.herd = herd()
        self.act_fleet_health = 0
        self.act_herd_health = 0


    def run_game(self):
        print('Game: Start!')
        self.greeting()
        self.game()
        
    def game(self):
        is_dead = False

        while is_dead == False:
            self.act_fleet_health = self.check_fleet_health()
            self.act_herd_health = self.check_herd_health()

            if self.act_fleet_health <= 0 or self.act_herd_health <= 0:
                is_dead = True
            if self.act_fleet_health <= 0:
                print(f'{self.herd.name} defeated {self.fleet.name}!')
            elif self.act_herd_health <= 0:
                print(f'{self.fleet.name} defeated {self.herd.name}!')
            if is_dead == True:
                self.ending()    

    def greeting(self):
        print(
            f'''
***********
Welcome to the world's most interesting game! The battlefield is set to {self.name}.
In the left corner, we have {self.fleet.name}! Complete with {self.fleet.optimus_prime.name},
{self.fleet.terminator.name}. and our very own {self.fleet.vision.name}!
And in the right corner, we have {self.herd.name}! Complete with a {self.herd.t_rex.name},
a {self.herd.spinosaurus.name}, and a {self.herd.stegosaurus.name}!
The stage is set! Let the games BEGIN!
***********            
            '''
        )
    
    def herd_dealt_dmg(self):
        chrg_dino = random.choice(self.herd.dinos)
        hurt_robot = random.choice(self.fleet.robots)
        att = self.herd.attack()
        print(f'{chrg_dino.name} used {att.name} and dealt {att.dmg} damage to {hurt_robot.name}')
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

    def fleet_dealt_dmg(self):
        chrg_rob = random.choice(self.fleet.robots)
        if chrg_rob == self.fleet.optimus_prime:
            att = self.op_dealt()
            return att
        elif chrg_rob == self.fleet.terminator:
            att = self.term_dealt()
            return att
        else:
            att = self.vis_dealt()
            return att

    def op_dealt(self):
        hurt_dino = random.choice(self.herd.dinos)
        att = self.fleet.op_attack()
        print(f'{self.fleet.optimus_prime.name} used {att.name} and dealt {att.dmg} to {hurt_dino.name}!')
        return att.dmg

    def term_dealt(self):
        hurt_dino = random.choice(self.herd.dinos)
        att = self.fleet.term_attack()
        print(f'{self.fleet.terminator.name} used {att.name} and dealt {att.dmg} to {hurt_dino.name}!')
        return att.dmg
    
    def vis_dealt(self):
        hurt_dino = random.choice(self.herd.dinos)
        att = self.fleet.vis_attack()
        print(f'{self.fleet.vision.name} used {att.name} and dealt {att.dmg} to {hurt_dino.name}!')
        return att.dmg

    def check_herd_health(self):
        herd_health = self.herd_health(self.act_herd_health)
        dmg_done = self.fleet_dealt_dmg()
        herd_health -= dmg_done
        return herd_health
    
    def herd_health(self, health_passed):
        herd_health = int(health_passed)
        if herd_health > 0:
            return herd_health
        else:    
            for dino in self.herd.dinos:
                herd_health += int(dino.health)
        return herd_health
 
    def ending(self):
        print('Thank you and good night!')
 