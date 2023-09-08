from button import Button
from text_input import Text_Input
import constants as C
import time

class Options:
    def __init__(self, app):
        self.app = app
        self.screen = app.screen

        self.btn_list = [
            Button(self.screen, C.pos_options_start, C.img_menu_start, 'start'),
            Button(self.screen, C.pos_options_easy, C.img_facile, 'easy'),
            Button(self.screen, C.pos_options_medium, C.img_moyen, 'medium'),
            Button(self.screen, C.pos_options_hard, C.img_difficile, 'hard'),
            Button(self.screen, C.pos_options_retour, C.img_menu_start, 'quit'),
            Button(self.screen, C.pos_options_1joueur, C.img_moyen, '1-player'),
            Button(self.screen, C.pos_options_2joueur, C.img_moyen, '2-player'),
        ]

        self.text_inputs = [
            #Text_Input(self.screen, )
        ]

    def update(self):
        self.button_events()

    def draw(self):
        for b in self.btn_list:
            b.draw()

    def button_events(self):
        for b in self.btn_list:
            b.update()
            if b.isClicked('start'):
                self.app.state = 'Game'
                self.app.game.reset()
                time.sleep(0.2)
                self.app.game.nom_joueurs = [self.app.menu.text_input.input.value,
                                             self.app.menu.text_input2.input.value]
            elif b.isClicked('easy'):
                # à faire
                pass

            elif b.isClicked('medium'):
                # à faire
                pass

            elif b.isClicked('hard'):
                # à faire
                pass

            elif b.isClicked('quit'):
                self.app.set_state('Menu')
