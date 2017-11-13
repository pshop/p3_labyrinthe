from ClassLabyrinthe import *
from ClassItem import *

labyrinthe1 = Labyrinthe("laby_setup.json", "laby")

aiguille = Item(labyrinthe1.empy_spaces, "aiguille")
labyrinthe1.add_item(aiguille.position, aiguille.name)

tube = Item(labyrinthe1.empy_spaces, "tube")
labyrinthe1.add_item(tube.position, tube.name)

ether = Item(labyrinthe1.empy_spaces, "ether")
labyrinthe1.add_item(ether.position, ether.name)

labyrinthe1.print_laby()
