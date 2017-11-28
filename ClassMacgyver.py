#! /usr/bin/env python3
# coding: utf-8

from ClassPerso import Perso


class Macgyver(Perso):

    def __init__(self, position):
        Perso.__init__(self, position)
        self.bag = []

    # not necessarily usefull but i thought it would fix an issue
    # Spoiler alert, it didn't
    def _get_position(self):
        return self._position

    def _set_position(self, new_position):
        self._position = new_position

    position = property(_get_position, _set_position)

    def move(self, next_item, next_position, maggy_pos, laby):
        """ maggy moves, puts items on his bag errase the X on its previous
        place and add a new X on the new place """

        if next_item == "T" or next_item == "E" or next_item == "A":
            self.bag.append(next_item)
        laby.add_item(maggy_pos, " ")
        laby.add_item(next_position, "X")

    def check_item(self, position, laby, usr_input):
        """ checks on the next position the item maggy will meet
        returns the item and the coord of the next pos"""
        if usr_input:
            if usr_input == "u" and position[0] > 0:
                coord = (position[0] - 1, position[1])
            elif usr_input == "d" and position[0] < 14:
                coord = (position[0] + 1, position[1])
            elif usr_input == "l" and position[1] > 0:
                coord = (position[0], position[1] - 1)
            elif usr_input == "r" and position[1] < 14:
                coord = (position[0], position[1] + 1)
            else:
                print("{} n'est pas une commande valide".format(usr_input))
                coord = False

            return laby.search_coord(coord), coord
        else:
            return False, False
