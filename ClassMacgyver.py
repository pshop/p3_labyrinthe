from ClassPerso import *

class Macgyver(Perso):

    def __init__(self, position):
        Perso.__init__(self, position)
        self.bag = []

    def move(self, usr_input):
        usr_input = usr_input.strip()
        usr_input = usr_input.lower()
        if usr_input == "up":
            self.position[0] -= 1
        elif usr_input == "down":
            self.position[0] += 1
        elif usr_input == "left":
            self.position[1] -= 1
        elif usr_input == "right":
            self.position[1] += 1
        else:
            print("{} n'est pas une commande valide".format(usr_input))
