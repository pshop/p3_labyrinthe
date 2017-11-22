import pygame

from pygame.locals import *
from app_macgyver_txt import AppText


        pygame.init()
        fenetre = pygame.display.set_mode((600, 600))
        fond = pygame.image.load("./img/fond.png").convert()
        fenetre.blit(fond, (0, 0))
        maggy = pygame.image.load("./img/maggy-2.png").convert_alpha()
        pos_maggy = maggy.get_rect()
        fenetre.blit(maggy, pos_maggy)

        pygame.display.flip()

        continuer = 1
        while continuer:
            for event in pygame.event.get():
                if event.type == QUIT:
                    continuer = 0
                if event.type == KEYDOWN:
                    if event.key == K_DOWN:
                        pos_maggy = pos_maggy.move(0, 40)
                    if event.key == K_UP:
                        pos_maggy = pos_maggy.move(0, -40)
                    if event.key == K_RIGHT:
                        pos_maggy = pos_maggy.move(40, 0)
                    if event.key == K_LEFT:
                        pos_maggy = pos_maggy.move(-40, 0)

            self.fenetre.blit(self.fond, (0, 0))
            self.fenetre.blit(self.maggy, self.pos_maggy)
            pygame.display.flip()
