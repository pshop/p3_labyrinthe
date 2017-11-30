#! /usr/bin/env python3
# coding: utf-8

from app_macgyver_gui import AppGUI
from app_macgyver_txt import AppText

def main():
    usr_input = True

    while usr_input:

        print("Bienvenue sur mon surper jeu !")
        print("Pour un maximum de texte lance la version console en tapant 1")
        print("Pour une immersion reversante (le vive n'a qu'a bien se tenir) tape 2")
        print("Pour quitter tape q")

        usr_input = input('>').strip()
        if usr_input == '1':
            new_game = AppText()
            new_game.start_app()
        elif usr_input == '2':
            new_game = AppGUI()
            new_game.start_GUI_app()
            usr_input = False
        elif usr_input == 'q':
            usr_input = False

if __name__ == '__main__':
    main()
