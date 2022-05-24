from Fleet import fleet

from Herd import herd

import random

class battlefield:
    def __init__(self, name):
        self.name = name
        self.fleet = fleet()
        self.herd = herd()
        pass

    def run_game(self):
        print('Game: Start!')
        self.greeting()
        self.game()
        
    def game(self):
        is_dead = False

        while is_dead == False:
            fleet()
            herd()
            self.charge()
            fleet_health = fleet.check_fleet_health(self)
            herd_health = herd.check_herd_health(self)
            if fleet_health == 0 or herd_health == 0:
                is_dead = True
            if fleet_health == 0:
                print(f'{fleet.name} defeated {herd.name}!')
            elif herd_health == 0:
                print(f'{herd.name} defeated {fleet.name}')
            if is_dead == True:
                self.ending()    

    def greeting(self):
        print(
            '''
***********

***********            
            '''
        )

    def ending(self):
        print('Thank you and good night!')
 
    def charge(self):
        
        pass

