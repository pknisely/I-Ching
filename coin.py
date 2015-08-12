# Import the random library for randomizing coin flip
import random

# Coin class definition
class Coin:
    def __init__(self, side_up = 'Heads'):
        self.side_up = side_up

    def __flip__(self):
        random_flip = random.randint(0,1)
        if random_flip == 0:
            self.side_up = 'Heads'
        else:
            self.side_up = 'Tails'

    def __get_side_up__(self):
        return self.side_up

    
    
