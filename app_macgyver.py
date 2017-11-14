from ClassLabyrinthe import *
from ClassItem import *
from ClassMacgyver import *
import os

##### INITIALISATION DU JEU ############
labyrinthe1 = Labyrinthe("laby_setup.json", "laby")
macgyver = Macgyver(labyrinthe1.macgyver_coord)
gardien = Perso(labyrinthe1.exit_coord)
############### Je suis sur que je peux faire mieux
aiguille = Item(labyrinthe1.empy_spaces, "aiguille")
labyrinthe1.add_item(aiguille.position, aiguille.name)

tube = Item(labyrinthe1.empy_spaces, "tube")
labyrinthe1.add_item(tube.position, tube.name)

ether = Item(labyrinthe1.empy_spaces, "ether")
labyrinthe1.add_item(ether.position, ether.name)
###############

#i print the labyrinthe on it's first state
labyrinthe1.print_laby()

########################################


while True:

    #i ask the user where to move
    print("Inventaire : ", macgyver.bag)
    usr_input = input("Faites bouger Macgyver: ")
    #i take the current maggy pos
    maggy_pos = labyrinthe1.macgyver_coord
    #now i take the next_item AND the next_pos
    next_item, next_coord = macgyver.check_item(maggy_pos, labyrinthe1, usr_input)
    if next_item == "S":
        break
    #if there is a next item (means not out of bound)
    #if the item is not a wall
    if next_item and next_item != "O":
        macgyver.move(next_item, next_coord, maggy_pos, labyrinthe1)
    #i print the new state of the laby
    labyrinthe1.print_laby()

os.system("clear")

if len(macgyver.bag) == 3:

    print("BRAVO ! vous avez gagné")
else:
    print("Le gardien a raison de vous, vous avez PERDU !")
