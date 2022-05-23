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
            self.charge()
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
 
    def charge():
        ''
