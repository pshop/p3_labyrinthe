import json

class Labyrinthe:

    def __init__(self, file, key):
        #load the labyrinthe from a json external file
        with open(file) as f:
            data = json.load(f)
            for entry in data:
                self.laby = entry[key]

    @property
    def empy_spaces(self):
        return self.search_items(" ")

    @property
    def macgyver_coord(self):
        return self.search_items("X")

    @property
    def exit_coord(self):
        return self.search_items("E")

    #I give an item i get coordonates
    def search_items(self, item):
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

    #I give coordonates, i get an item_pos
    def search_coord(self, coord):
        return self.laby[coord[0]][coor[1]]


    #I give coordonates item_pos and i put the char item_name
    #at this place
    def add_item(self,item_pos, item_name):
        self.laby[item_pos[0]][item_pos[1]] = item_name[0]

    #I slimply print the labyrinthe at it's current state
    def print_laby(self):
        for line in self.laby:
            for sprite in line:
                print(sprite, end = "")
            print()

    def chk_next(self, position):
        pass


if __name__ == "__main__":
    pass
