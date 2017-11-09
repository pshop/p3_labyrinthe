class Labyrinthe:

    def __init__(self):
        self.laby = [\
        [" "," ","O","O","O","O","O","O","O","O","O","O","O","O","O"],
        ["O"," ","O"," "," "," "," "," "," "," ","O","O"," "," "," "],
        ["O"," ","O"," ","O","O","O","O","O"," ","O","O"," ","O","O"],
        ["O"," ","O"," ","O"," "," "," ","O"," ","O","O"," ","O","O"],
        ["O"," ","O"," ","O"," ","O"," ","O"," "," "," "," ","O","O"],
        ["O"," ","O"," ","O"," ","O"," ","O","O","O","O"," ","O","O"],
        ["O"," ","O"," ","O"," ","O"," ","O"," ","O","O"," ","O","O"],
        [" "," "," "," ","O"," ","O"," ","O"," ","O","O"," ","O"," "],
        ["O","O","O","O","O"," ","O"," "," "," "," "," "," ","O"," "],
        [" "," "," ","O","O"," ","O","O","O"," ","O","O","O","O"," "],
        [" ","O"," ","O","O"," ","O","O","O"," ","O"," "," "," "," "],
        [" ","O"," ","O"," "," ","O"," "," "," ","O","O","O"," ","O"],
        [" ","O"," ","O","O"," ","O"," ","O"," ","O","O","O"," ","O"],
        [" ","O"," "," "," "," ","O"," ","O"," "," "," ","O"," ","O"],
        [" ","O","O","O"," "," ","O"," ","O","O","O"," "," "," ","O"]]

        self.macgyver = (14,0)
        self.finish = (1, 14)

    @property
    def empy_spaces(self):
        line_nb = 0
        sprite_nb = 0
        empty_coordonates = []
        #add the macgyver and the exit
        #fils the list empty_coordonates
        for line in self.laby:
            for sprite in line:
                pos = (line_nb, sprite_nb)
                #if coordonates are the same as macgyvers
                if pos == self.macgyver:
                    self.laby[line_nb][sprite_nb] = "X"
                #if coordonates are the same as the finish
                elif pos == self.finish:
                    self.laby[line_nb][sprite_nb] = "E"
                #if the pos is free, i fell the empty_coordonates
                if self.laby[line_nb][sprite_nb] == " ":
                    empty_coordonates.append(pos)
                sprite_nb += 1
            sprite_nb = 0
            line_nb += 1
        return empty_coordonates

    def print_laby(self):
        #print the entire laby
        for line in self.laby:
            for sprite in line:
                print(sprite, end = "")
            print()

def main():
    labyrinthe1 = Labyrinthe()
    empty_pos = labyrinthe1.empy_spaces
    labyrinthe1.print_laby()
    print(empty_pos)

main()
