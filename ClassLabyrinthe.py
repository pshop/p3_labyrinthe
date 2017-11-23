import json

class Labyrinthe:

    def __init__(self, file):
        """ give a json file with a labyrinthe base on the model
        laby_setup.json"""
        #load the labyrinthe from a json external file
        with open(file) as f:
            self.laby = json.load(f)

    @property
    def empy_spaces(self):
        """returns a list of tuples with the coordonates of all space char"""
        return self.search_items(" ")

    @property
    def macgyver_coord(self):
        """ returns the coordonates of macgyver """
        return self.search_items("X")

    @property
    def exit_coord(self):
        """ returns the coordonates of the exit """
        return self.search_items("S")

    @property
    def tab_laby(self):
        """ return the list of list of the current state of the laby"""
        return self.laby

    def search_items(self, item):
        """ I give an item i get coordonates """
        items_coordonates = []
        #fils the list empty_coordonates
        for line_nb, line_value in enumerate(self.laby):
            for sprite_nb, sprite_value in enumerate(line_value):
                pos = [line_nb, sprite_nb]
                #if the pos is free, i fell the empty_coordonates
                if sprite_value == item:
                    items_coordonates.append(pos)
        if len(items_coordonates) == 1:
            return items_coordonates[0]
        else:
            return items_coordonates


    def search_coord(self, coord):
        """I give coordonates, i get an item_pos"""
        if coord:
            return self.laby[coord[0]][coord[1]]
        else:
            return False

    def add_item(self,item_pos, item_name):
        """ I give coordonates item_pos and i put the char item_name
        at this place in the laby"""
        self.laby[item_pos[0]][item_pos[1]] = item_name[0]

    def print_laby(self):
        """ I slimply print the labyrinthe at it's current state """
        for line in self.laby:
            for sprite in line:
                print(sprite, end = "")
            print()
