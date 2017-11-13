import json

class Labyrinthe:

    def __init__(self, file, key):
        with open(file) as f:
            data = json.load(f)
            for entry in data:
                self.laby = entry[key]

    @property
    def empy_spaces(self):

        empty_coordonates = []
        #fils the list empty_coordonates
        for line_nb, line_value in enumerate(self.laby):
            for sprite_nb, sprite_value in enumerate(line_value):
                pos = (line_nb, sprite_nb)
                #if the pos is free, i fell the empty_coordonates
                if sprite_value == " ":
                    empty_coordonates.append(pos)
        return empty_coordonates

    @property
    def macgyver_coord(self):
        pass

    @property
    def exit_coord(self):
        pass

    def print_laby(self):
        #print the entire lab
        ##### needs the 3 obj_coor
        for line in self.laby:
            for sprite in line:
                print(sprite, end = "")
            print()

def main():
    labyrinthe1 = Labyrinthe("laby_setup.json", "laby")
    empty_pos = labyrinthe1.empy_spaces
    labyrinthe1.print_laby()
    print(empty_pos)

main()
