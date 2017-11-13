from ClassLabyrinthe import *
from ClassItem import *
from ClassMacgyver import *
import os

##### INITIALISATION DU JEU ############
labyrinthe1 = Labyrinthe("laby_setup.json", "laby")
macgyver = Macgyver(labyrinthe1.macgyver_coord)
############### Je suis sur que je peux faire mieux
aiguille = Item(labyrinthe1.empy_spaces, "aiguille")
labyrinthe1.add_item(aiguille.position, aiguille.name)

tube = Item(labyrinthe1.empy_spaces, "tube")
labyrinthe1.add_item(tube.position, tube.name)

ether = Item(labyrinthe1.empy_spaces, "ether")
labyrinthe1.add_item(ether.position, ether.name)
###############

#j'affiche une première fois le labyrinthe
labyrinthe1.print_laby()

########################################


while True:

    labyrinthe1.add_item(macgyver.position, " ")
    usr_input = input("Faites bouger Macgyver: ")
    macgyver.move(usr_input)
    labyrinthe1.add_item(macgyver.position, "X")
    os.system('clear')
    labyrinthe1.print_laby()
