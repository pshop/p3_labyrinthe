from ClassPerso import *

class Macgyver(Perso):

    def __init__(self, position):
        Perso.__init__(self, position)
        self.bag = []

    def move(self, usr_input, laby):
        usr_input = usr_input.strip()
        usr_input = usr_input.lower()
        next_position = self.next_pos(self.position, usr_input[0])
        next_item = self.check_next(next_position[0], next_position[1], laby)

        if next_item != "O":
            if next_item == "T" or next_item == "E" or next_item == "A":
                self.bag.append(next_item)
            self.position = next_position
            laby.add_item(self.position, "X")

    def check_next(self, x, y, laby):
        coord = (x, y)
        next_item = laby.search_coord(coord)
        return next_item

    def next_pos(self, position, usr_input):
        if usr_input == "u" and position[0] > 0:
            position[0] -= 1
        elif usr_input == "d" and position[0] < 14:
            position[0] += 1
        elif usr_input == "l" and position[1] > 0:
            position[1] -= 1
        elif usr_input == "r" and position[1] < 14:
            position[1] += 1
        else:
            print("{} n'est pas une commande valide".format(usr_input))
        return position
