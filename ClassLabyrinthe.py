import json

class Labyrinthe:

    def __init__(self, file, key):
        #load the labyrinthe from a json external file
        with open(file) as f:
            data = json.load(f)
            for entry in data:
                self.laby = entry[key]

    def search_items(self, item):
        items_coordonates = []
        #fils the list empty_coordonates
        for line_nb, line_value in enumerate(self.laby):
            for sprite_nb, sprite_value in enumerate(line_value):
                pos = (line_nb, sprite_nb)
                #if the pos is free, i fell the empty_coordonates
                if sprite_value == item:
                    items_coordonates.append(pos)
        return items_coordonates

    @property
    def empy_spaces(self):
        return self.search_items(" ")

    @property
    def macgyver_coord(self):
        return self.search_items("X")

    @property
    def exit_coord(self):
        return self.search_items("E")

    def print_laby(self):
        #print the entire lab
        ##### needs the 3 obj_coor
        for line in self.laby:
            for sprite in line:
                print(sprite, end = "")
            print()

if __name__ == "__main__":
    pass
