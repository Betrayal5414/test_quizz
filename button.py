import pygame
import time

class Button:
    def __init__(self, screen, x, y, path="img/boutons/reponses/rep_nopush_bleu.png"):
        self.screen = screen
        self.x = x
        self.y = y
        self.img_path = path

        # load images
        self.unpushed_img = pygame.image.load(self.img_path)
        self.pushed_img = pygame.image.load("img/boutons/reponses/rep_push_bleu.png")

        # initialise width et height selon la taille de l'image
        self.w = self.unpushed_img.get_width()
        self.h = self.unpushed_img.get_height()

        self.pushed = False
        self.t = 0

    def update(self):
        # button press 'animation', button stay pushed for 0.5s (30frames)
        if self.pushed: self.t += 1
        if self.t > 30:
            self.pushed = False
            self.t = 0

    def draw(self):
        # affiche la bonne image selon si le bouton est pressé ou non
        if self.pushed:
            self.screen.blit(self.pushed_img, (self.x, self.y))
        else:
            self.screen.blit(self.unpushed_img, (self.x, self.y))

    def checkForClick(self, event):
        x, y = pygame.mouse.get_pos()
        if x > self.x and x < self.x + self.w and y > self.y and y < self.y + self.h:
            self.pushed = True
        return x > self.x and x < self.x + self.w and y > self.y and y < self.y + self.h
