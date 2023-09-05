import pygame
from button import Button
import constants as C

class Menu:
    # constructeur
    def __init__(self, screen):
        # get app's screen to draw on
        self.screen = screen

        self.background_img = pygame.image.load("img/menu_principal.png")
        self.btn_list = [
            Button(self.screen, 1050, 500, "img/boutons/menu/menu_nopush.png"),

        ]

    # method update, appelée chaque frame (60fois par sec)
    def update(self):
        for b in self.btn_list:
            b.update()

    # method draw, appelée après l'update
    def draw(self):
        self.screen.blit(self.background_img, (0,0))
        for b in self.btn_list:
            b.draw()
        # start button text
        C.blit_text(self.screen, "Start", C.start_text_pos, 280, C.font_karmatic, '#101010')
