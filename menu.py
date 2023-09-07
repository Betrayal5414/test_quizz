import pygame
from button import Button
import constants as C
from text_input import Text_Input

class Menu:
    # constructeur
    def __init__(self, app):
        # get app's screen to draw on
        self.app = app
        self.screen = app.screen

        self.app.cursor.execute(f"SELECT intitule_diff FROM difficulte WHERE difficulte_id < 4")
        self.diff_names = self.app.cursor.fetchall()
        print(self.diff_names)

        self.background_img = C.img_menu_background
        self.btn_list = [
            Button(self.screen, 1025, 500, C.img_menu_start, 'start'),
            Button(self.screen, 1000, 400, C.img_facile, 'easy'),
            Button(self.screen, 1080, 400, C.img_moyen, 'medium'),
            Button(self.screen, 1160, 400, C.img_difficile, 'hard'),
        ]
        self.text_input = Text_Input(self.app, 50, 480)
        self.text_input2 = Text_Input(self.app, 50, 565)

    # method update, appelée chaque frame (60fois par sec)
    def update(self, events):
        for b in self.btn_list:
            b.update()
        self.text_input.update(events)
        self.text_input2.update(events)



    # method draw, appelée après l'update
    def draw(self):
        self.screen.blit(self.background_img, (0,0))
        for b in self.btn_list:
            b.draw()
        # start button text
        C.blit_text(self.screen, "Start", C.start_text_pos, 280, C.font_karmatic, '#101010')
        # difficulté text
        C.blit_text(self.screen, f"Difficulté: {self.diff_names[self.app.difficulte-1][0]}", (1015,360), C.WIN_X, C.font_pixelop8, 'white')
        self.text_input.draw()
        self.text_input2.draw()
