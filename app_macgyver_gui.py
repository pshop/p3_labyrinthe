import pygame
import os

from pygame.locals import *
from ClassLabyrinthe import Labyrinthe
from ClassItem import Item
from ClassMacgyver import Macgyver
from ClassPerso import Perso

pygame.init()
fenetre = pygame.display.set_mode((600, 600))

###IMAGES
fond_img = pygame.image.load("./img/fond.png").convert()
maggy_img = pygame.image.load("./img/maggy-2.png").convert_alpha()
guard_img = pygame.image.load("./img/gardien.png").convert_alpha()
wall_img = pygame.image.load("./img/wall.png").convert()
dart_img = pygame.image.load("./img/dart.png").convert_alpha()
tube_img = pygame.image.load("./img/tube.png").convert_alpha()
eth_img = pygame.image.load("./img/eth.png").convert_alpha()

def to_gui_scale(position):
    new_pos = []
    for i in position:
        new_pos.insert(0, i * 40)
    return new_pos


##### INITIALISATION DU JEU ############
labyrinthe1 = Labyrinthe("laby_setup.json", "laby")
# # verifier si j'utilise bien la position de macgiver
macgyver = Macgyver(labyrinthe1.macgyver_coord)
pos_maggy = to_gui_scale(macgyver.position)

gardien = Perso(labyrinthe1.exit_coord)
pos_guard = to_gui_scale(labyrinthe1.exit_coord)

aiguille = Item(labyrinthe1.empy_spaces, "aiguille")
labyrinthe1.add_item(aiguille.position, aiguille.name)
pos_dart = to_gui_scale(aiguille.position)

tube = Item(labyrinthe1.empy_spaces, "tube")
labyrinthe1.add_item(tube.position, tube.name)
pos_tube = to_gui_scale(tube.position)

ether = Item(labyrinthe1.empy_spaces, "ether")
labyrinthe1.add_item(ether.position, ether.name)
pos_eth = to_gui_scale(ether.position)
#########################################
labyrinthe1.print_laby()

continuer = 1
while continuer:

    usr_input = False
    next_item = False
    next_coord = [0,0]
    fenetre.blit(fond_img, (0, 0))

    for event in pygame.event.get():
        if event.type == QUIT:
            continuer = 0
        if event.type == KEYDOWN:
            if event.key == K_DOWN:
                usr_input = 'd'
            if event.key == K_UP:
                usr_input = 'u'
            if event.key == K_RIGHT:
                usr_input = 'r'
            if event.key == K_LEFT:
                usr_input = 'l'

            maggy_tab_pos = labyrinthe1.macgyver_coord
            print(maggy_tab_pos)
            # now i take the next_item AND the next_pos
            next_item, next_coord = macgyver.check_item(maggy_tab_pos, labyrinthe1, usr_input)

    if next_item == "S":
        continuer = 0
    # if there is a next item (means not out of bound)
    # if the item is not a wall
    if next_item and next_item != "O":
        macgyver.move(next_item, next_coord, maggy_tab_pos, labyrinthe1)
        macgyver.position = next_coord



    for line in range(len(labyrinthe1.tab_laby)):
        for column in range(len(labyrinthe1.tab_laby[line])):
            if labyrinthe1.tab_laby[line][column] == 'O':
                pos = [line, column]
                pos_wall = to_gui_scale(pos)
                fenetre.blit(wall_img, pos_wall)

    fenetre.blit(maggy_img, to_gui_scale(macgyver.position))
    fenetre.blit(guard_img, pos_guard)
    if labyrinthe1.search_coord(tube.position) == 'T':
        fenetre.blit(tube_img, pos_tube)
    if labyrinthe1.search_coord(aiguille.position) == 'A':
        fenetre.blit(dart_img, pos_dart)
    if labyrinthe1.search_coord(ether.position) == 'E':
        fenetre.blit(eth_img, pos_eth)
    pygame.display.flip()
