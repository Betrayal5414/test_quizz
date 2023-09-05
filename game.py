from timer_bar import Timer_Bar
import pygame
from button import Button
import constants as C
import random

class Game:
    def __init__(self, app, cursor, diff):
        # get app's screen to draw on
        self.app = app
        self.screen = app.screen
        # load background image
        self.ingame_img = pygame.image.load("img/questions/fond_bleu.png")
        # initialize timer-bars and buttons
        self.timer = Timer_Bar(self.screen, 40, 70, 15, C.colors['Blue'])
        self.answers_buttons = [
            Button(self.screen, 40, C.WIN_Y - 100),
            Button(self.screen, 340, C.WIN_Y - 100),
            Button(self.screen, 640, C.WIN_Y - 100),
            Button(self.screen, 940, C.WIN_Y - 100)
        ]
        self.back_button = Button(self.screen, C.WIN_X-300, 40)

        # question-answers attributes
        self.answer_index = 0
        self.question_i = 0
        self.max_index = 39

        # récupère les questions dans la DB
        self.cursor = cursor
        self.cursor.execute(f"SELECT * FROM questions WHERE difficulte = {diff}")
        self.liste_questions = self.cursor.fetchall()
        # choisis une question
        self.next_question()

        # initialize text surface for "Question 1"
        self.question_title_surface = pygame.surface.Surface((390,215))

        # temp vars, will change soon
        self._score = 0

    def update(self):
        self.timer.update()
        for b in self.answers_buttons:
            b.update()
        self.back_button.update()

        if not self.answer_index == 0:
            if self.answer_index == self.bonne_reponse + 1:
                print("GG!")
                self.next_question()
                self.timer.reset()
                self._score += 10
            self.answer_index = 0



    def draw(self):
        self.screen.blit(self.ingame_img, (0,0))
        self.timer.draw()
        for b in self.answers_buttons:
            b.draw()
        self.back_button.draw()

        # texte numéro question
        self.txt_surface = C.font_karmatic.render(f"Question  {self.question_i}", False, (0, 0, 0))
        self.screen.blit(self.txt_surface, C.question_number_pos)
        # intitulé question
        C.blit_text(self.screen, self.current_question[1], (C.question_title_pos), 430, C.font_pixelop8, 'black')
        # affichage texte réponses
        for i, r in enumerate(self.liste_reponses):
            C.blit_text(self.screen, r[1], (70+300*i, 650), 280+300*i, C.font_pixelop8small, 'white')

        # affichage score
        C.blit_text(self.screen, str(self._score), (C.WIN_X-100, 130), C.WIN_X, C.font_karmatic, 'white')

        # texte bouton retour menu
        C.blit_text(self.screen, 'Quit', C.quit_text_pos, 280, C.font_karmatic, '#b01010')


    def next_question(self):
        # get random question in list
        self.current_question = self.liste_questions[random.randint(0,self.max_index)]
        # remove given question from list
        self.liste_questions.remove(self.current_question)
        # increment/decrement variables
        self.max_index -= 1
        self.question_i += 1
        # get the 4 adequate answers from DB
        self.cursor.execute(f"SELECT * FROM reponses WHERE question_id = {self.current_question[0]}")
        self.liste_reponses = self.cursor.fetchall()
        # find right answer
        for i, r in enumerate(self.liste_reponses):
            if r[2] == 1:
                self.bonne_reponse = i
        # reset timer bar
        self.timer.reset()
        # si il n'y a plus de question, retour menu et reset liste
        if self.max_index < 0:
            self.cursor.execute(f"SELECT * FROM questions WHERE difficulte = 2")
            self.liste_questions = self.cursor.fetchall()
            self.max_index = 39
            self.question_i = 0
            self.app.state = 'Menu'
