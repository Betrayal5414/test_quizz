import pygame
import time

class Button:
    def __init__(self, screen, x, y, img, name=""):
        self.screen = screen
        self.x = x
        self.y = y
        self.name = name
        self.clickedOnce = False

        # load images
        self.unpushed_img = img
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

    def checkForClick(self):
        x, y = pygame.mouse.get_pos()
        return x > self.x and x < self.x + self.w and y > self.y and y < self.y + self.h

    def isClicked(self, name=""):
        if name == "":
            pass
        else:
            if self.name != name:
                return False
        # if pressed, return true once and change clickedOnce to false until not pressed anymore
        if pygame.mouse.get_pressed()[0] and self.checkForClick():
            if not self.clickedOnce:
                self.clickedOnce = True
                self.pushed = True
                return True
            else:
                return False
        else:
            self.clickedOnce = False
            return False