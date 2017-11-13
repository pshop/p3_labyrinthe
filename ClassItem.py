import random
from ClassLabyrinthe import *

class Item:

    def __init__(self, empty_spaces, name):
        self.position = random.choice(empty_spaces)
        self.picked = False
        self.name = name.capitalize()
