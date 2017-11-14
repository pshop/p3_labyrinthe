from ClassPerso import *

class Macgyver(Perso):

    def __init__(self, position):
        Perso.__init__(self, position)
        self.bag = []

    def _get_position(self):
        return self._position

    def _set_position(self, new_position):
        self._position = new_position

    position = property(_get_position, _set_position)

    def move(self, next_item, next_position, laby):
        #if the user didn't write anything

        ###if usr_input == "":
            ###usr_input = "x"

        #cleaning the input

        ###usr_input = usr_input.strip()
        ###usr_input = usr_input.lower()

        ########
        ### I think that here is the mistake the goal is to
        ### check what item is at the next position without moving
        ### maggy and moving him or not depending on the next item
        ########

        # So i use the function next_pos to get the coords of the next move

        ###next_position = self.next_pos(self.position, usr_input[0])

        # Now i got the next coord i get the item at these coord

        ###next_item = self.check_item(next_position, laby)

        if next_item == "T" or next_item == "E" or next_item == "A":
            self.bag.append(next_item)
        self.position = next_position
        laby.add_item(self.position, "X")



    def check_item(self, laby, usr_input):

        if usr_input == "u" and self.position[0] > 0:
            coord = (self.position[0] - 1, self.position[1])
        elif usr_input == "d" and selfself.position[0] < 14:
            coord = (self.position[0] + 1, self.position[1])
        elif usr_input == "l" and self.position[1] > 0:
            coord = (self.position[0], self.position[1] - 1)
        elif usr_input == "r" and self.position[1] < 14:
            coord = (self.position[0], self.position[1] + 1)
        else:
            print("{} n'est pas une commande valide".format(usr_input))

        return laby.search_coord(coord)

        # next_item = laby.search_coord(next_position)
        # return next_item

    def next_pos(self, position, usr_input):
        if usr_input == "u" and position[0] > 0:
            position[0] -= 1
        elif usr_input == "d" and position[0] < 14:
            position[0] += 1
        elif usr_input == "l" and position[1] > 0:
            position[1] -= 1
        elif usr_input == "r" and position[1] < 14:
            position[1] += 1
        return position
