import random

class Item:

    def __init__(self, empty_spaces, name):
        self.position = random.choice(empty_spaces)
        self.name = name.capitalize()
