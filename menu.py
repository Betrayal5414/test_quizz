import pygame
from button import Button
import constants as C

class Menu:
    def __init__(self, screen):
        self.screen = screen
        self.background_img = pygame.image.load("img/menu_principal.png")
        self.button = Button(self.screen, 1050, 500, "img/boutons/menu/menu_nopush.png")

    def update(self):
        self.button.update()

    def draw(self):
        self.screen.blit(self.background_img, (0,0))
        # start button
        self.button.draw()
        C.blit_text(self.screen, "Start", C.start_text_pos, 280, C.font_karmatic, '#101010')
