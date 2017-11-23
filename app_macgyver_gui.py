import pygame
import os

from pygame.locals import *
from ClassLabyrinthe import Labyrinthe
from ClassItem import Item
from ClassMacgyver import Macgyver
from ClassPerso import Perso


class AppGUI:

    def __init__(self):
        pygame.init()
        self.fenetre = pygame.display.set_mode((600, 600))

        # ##IMAGES
        self.fond_img = pygame.image.load("./img/fond.png").convert()
        self.maggy_img = pygame.image.load("./img/maggy-2.png").convert_alpha()
        self.guard_img = pygame.image.load("./img/gardien.png").convert_alpha()
        self.wall_img = pygame.image.load("./img/wall.png").convert()
        self.dart_img = pygame.image.load("./img/dart.png").convert_alpha()
        self.tube_img = pygame.image.load("./img/tube.png").convert_alpha()
        self.eth_img = pygame.image.load("./img/eth.png").convert_alpha()
        self.gameover_img = pygame.image.load("./img/go.jpeg").convert()
        self.win_img = pygame.image.load("./img/win.png").convert()

        # #### INITIALISATION DU JEU ############
        self.labyrinthe1 = Labyrinthe("laby_setup.json")
        # # verifier si j'utilise bien la position de macgiver
        self.macgyver = Macgyver(self.labyrinthe1.macgyver_coord)
        self.pos_maggy = self.to_gui_scale(self.macgyver.position)

        self.gardien = Perso(self.labyrinthe1.exit_coord)
        self.pos_guard = self.to_gui_scale(self.labyrinthe1.exit_coord)

        self.aiguille = Item(self.labyrinthe1.empy_spaces, "aiguille")
        self.labyrinthe1.add_item(self.aiguille.position, self.aiguille.name)
        self.pos_dart = self.to_gui_scale(self.aiguille.position)

        self.tube = Item(self.labyrinthe1.empy_spaces, "tube")
        self.labyrinthe1.add_item(self.tube.position, self.tube.name)
        self.pos_tube = self.to_gui_scale(self.tube.position)

        self.ether = Item(self.labyrinthe1.empy_spaces, "ether")
        self.labyrinthe1.add_item(self.ether.position, self.ether.name)
        self.pos_eth = self.to_gui_scale(self.ether.position)
        # ########################################

    def to_gui_scale(self, position):
        new_pos = []
        for i in position:
            new_pos.insert(0, i * 40)
        return new_pos

    def start_GUI_app(self):
        continuer = 1
        while continuer:

            usr_input = False
            next_item = False
            next_coord = [0, 0]
            self.fenetre.blit(self.fond_img, (0, 0))

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

                    maggy_tab_pos = self.labyrinthe1.macgyver_coord
                    # now i take the next_item AND the next_pos
                    next_item, next_coord = self.macgyver.check_item(maggy_tab_pos, self.labyrinthe1, usr_input)

            if next_item == "S":
                continuer = self.end_game()
            # if there is a next item (means not out of bound)
            # if the item is not a wall
            if next_item and next_item != "O":
                self.macgyver.move(next_item, next_coord, maggy_tab_pos, self.labyrinthe1)
                self.macgyver.position = next_coord

            for line in range(len(self.labyrinthe1.tab_laby)):
                for column in range(len(self.labyrinthe1.tab_laby[line])):
                    if self.labyrinthe1.tab_laby[line][column] == 'O':
                        pos_wall = self.to_gui_scale([line, column])
                        self.fenetre.blit(self.wall_img, pos_wall)

            self.fenetre.blit(self.maggy_img, self.to_gui_scale(self.macgyver.position))
            self.fenetre.blit(self.guard_img, self.pos_guard)
            if self.labyrinthe1.search_coord(self.tube.position) == 'T':
                self.fenetre.blit(self.tube_img, self.pos_tube)
            if self.labyrinthe1.search_coord(self.aiguille.position) == 'A':
                self.fenetre.blit(self.dart_img, self.pos_dart)
            if self.labyrinthe1.search_coord(self.ether.position) == 'E':
                self.fenetre.blit(self.eth_img, self.pos_eth)
            pygame.display.flip()

    def end_game(self):
        continuer = 1
        while continuer:

            for event in pygame.event.get():
                if event.type == QUIT:
                    continuer = 0

            if len(self.macgyver.bag) == 3:
                self.fenetre.blit(self.win_img, (0, 0))
            else:
                self.fenetre.blit(self.gameover_img, (0, 0))
            pygame.display.flip()
        return continuer


# gui_session = AppGUI()
# gui_session.start_GUI_app()
