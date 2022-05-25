from Battlefield import battlefield

import random

choices = ['desert', 'island', 'city', 'field', 'volcanoes']

bf = battlefield(random.choice(choices))

bf.run_game()
