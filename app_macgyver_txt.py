#! /usr/bin/env python3
# coding: utf-8

import os

from ClassLabyrinthe import Labyrinthe
from ClassItem import Item
from ClassMacgyver import Macgyver
from ClassPerso import Perso


class AppText:

    def __init__(self):

        # #### INITIALISATION DU JEU ############
        self.labyrinthe1 = Labyrinthe("laby_setup.json")
        
        self.macgyver = Macgyver(self.labyrinthe1.macgyver_coord)
        self.gardien = Perso(self.labyrinthe1.exit_coord)

        self.aiguille = Item(self.labyrinthe1.empy_spaces, "aiguille")
        self.labyrinthe1.add_item(self.aiguille.position, self.aiguille.name)

        self.tube = Item(self.labyrinthe1.empy_spaces, "tube")
        self.labyrinthe1.add_item(self.tube.position, self.tube.name)

        self.ether = Item(self.labyrinthe1.empy_spaces, "ether")
        self.labyrinthe1.add_item(self.ether.position, self.ether.name)

        # i print the labyrinthe on it's first state
        self.labyrinthe1.print_laby()

    def start_app(self):

        while True:

            # i ask the user where to move
            print("Inventaire : ", self.macgyver.bag)
            # 'q' pour quitter
            usr_input = input("Faites bouger Macgyver: ")
            if usr_input == 'q' or usr_input == 'quit':
                break
            # i take the current maggy pos
            maggy_pos = self.labyrinthe1.macgyver_coord
            # now i take the next_item AND the next_pos
            next_item, next_coord = self.macgyver.check_item(maggy_pos, self.labyrinthe1, usr_input)
            if next_item == "S":
                break
            # if there is a next item (means not out of bound)
            # if the item is not a wall
            if next_item and next_item != "O":
                self.macgyver.move(next_item, next_coord, maggy_pos, self.labyrinthe1)
            # i print the new state of the laby
            self.labyrinthe1.print_laby()

        os.system("clear")

        if usr_input == 'q' or usr_input == 'quit':
            print('A dieu')
        elif len(self.macgyver.bag) == 3:
            print("BRAVO ! vous avez gagné\n\n")
        else:
            print("Le gardien a raison de vous, vous avez PERDU !\n\n")

def main():
    new_game = AppText()
    new_game.start_app()

if __name__ == '__main__':
    main()
