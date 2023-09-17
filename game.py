from timer_bar import Timer_Bar
import pygame
from button import Button
import constants as C
import random

class Game:
    def __init__(self, app):
        # get app's screen to draw on
        self.app = app
        self.screen = app.screen
        # sounds
        pygame.mixer.init()
        self.sound_juste = pygame.mixer.Sound("sounds/juste.wav")
        self.sound_faux = pygame.mixer.Sound("sounds/faux.wav")
        # initialize timer-bars and buttons
        self.timer = Timer_Bar(self.screen, 40, 70, C.time_per_question, C.colors['Blue'])
        self.answers_buttons = [
            Button(self.screen, (40, C.WIN_Y - 100), C.img_reponse),
            Button(self.screen, (340, C.WIN_Y - 100), C.img_reponse),
            Button(self.screen, (640, C.WIN_Y - 100), C.img_reponse),
            Button(self.screen, (940, C.WIN_Y - 100), C.img_reponse)
        ]
        self.back_button = Button(self.screen, (C.WIN_X-300, 40), C.img_reponse)

        # question-answers attributes
        self.answer_index = 0
        self.question_i = 0
        self.max_index = 39

        # récupère les questions dans la DB
        self.cursor = self.app.cursor

        # var utilisée pour délayer l'appuie sur 'quitter' après l'entrée en jeu
        self.back_button_timer = 0

        # initialize text surface for "Question 1"
        self.question_title_surface = pygame.surface.Surface((390,215))

        # couleurs de fond possibles
        self.possible_colors = ['blue', 'green', 'cyan', 'yellow', 'grey', 'orange', 'red', 'purple']
        self.background_color = random.choice(self.possible_colors)

        # load background image
        self.ingame_img = pygame.image.load(f"img/background/questions/fond_{self.background_color}.png")

        # noms joueurs et scores
        self.nom_joueurs = ["",""]
        self.scores = [0, 0]
        self.current_player = 0
        self.nbr_players = 1

        self.icone_j1 = None
        self.icone_j2 = None

        # choisis une question
        self.reset()


    def update(self):
        self.timer.update()
        for b in self.answers_buttons:
            b.update()
        self.back_button.update()

        # vérifie si l'user a appuyé sur une réponse et si c'est la bonne
        if not self.answer_index == 0:
            if self.answer_index == self.bonne_reponse + 1:
                # get score depending on time spent
                self.scores[self.current_player] += max(round(
                    C.max_points * (self.timer.chrono/self.timer.sec)), C.min_points)
                self.next_question()
                self.timer.reset()
                self.sound_juste.play()
            else:
                self.next_question()
                self.timer.reset()
                self.sound_faux.play()
            self.answer_index = 0

        if self.timer.chrono <= 0:
            self.next_question()
            self.timer.reset()

        if self.question_i > 10:
            self.end()


    def draw(self):
        self.screen.blit(self.ingame_img, (0,0))
        self.timer.draw()
        for b in self.answers_buttons:
            b.draw()
        self.back_button.draw()

        # texte numéro question
        self.txt_surface = C.font_karmatic30.render(f"Question  {self.question_i}", False, (0, 0, 0))
        self.screen.blit(self.txt_surface, C.pos_question_number)
        # intitulé question
        C.blit_text(self.screen, self.current_question[1], (C.pos_question_title), 430, C.font_pixelop8, 'black')
        # affichage texte réponses
        for i, r in enumerate(self.liste_reponses):
            C.blit_text(self.screen, r[1], (70+300*i, 650), 280+300*i, C.font_pixelop8small, 'white')
        # affichage nom joueur en cours
        if self.nbr_players == 2:
            C.blit_text(self.screen, f"{self.nom_joueurs[self.current_player]}", (C.WIN_X/6, 14), C.WIN_X/1.4, C.font_karmatic30, self.background_color)
        # affichage scores
        C.blit_text(self.screen, f"{self.nom_joueurs[0]} : {self.scores[0]}",
                    C.pos_game_score_1, C.WIN_X, C.font_karmatic20, 'white')
        if self.nbr_players == 2:
            C.blit_text(self.screen, f"{self.nom_joueurs[1]} : {self.scores[1]}",
                        C.pos_game_score_2, C.WIN_X, C.font_karmatic20, 'white')

        # texte bouton retour menu
        C.blit_text(self.screen, 'Quit', C.pos_quit_text, 280, C.font_karmatic30, '#b01010')

        # affichage texte difficulté


    def next_question(self):
        # get random question in list
        self.current_question = self.liste_questions[random.randint(0,self.max_index)]
        # remove given question from list
        self.liste_questions.remove(self.current_question)
        # increment/decrement variables
        self.max_index -= 1
        self.question_i += 1
        if self.nom_joueurs[1] != "":
            self.current_player = 1- self.current_player
        # get the 4 adequate answers from DB
        self.cursor.execute(f"SELECT * FROM reponses WHERE questions_id = {self.current_question[0]}")
        self.liste_reponses = self.cursor.fetchall()
        # find right answer
        for i, r in enumerate(self.liste_reponses):
            if r[2] == 1:
                self.bonne_reponse = i
        # reset timer bar
        self.timer.reset()
        # si il n'y a plus de question, retour menu et reset liste
        if self.max_index < 0:
            self.end()

    def reset(self):
        # récupère la difficulté depuis l'app
        self.diff = self.app.difficulte
        # récupère les questions de la bonne difficulté dans la BDD
        self.cursor.execute(f"SELECT * FROM questions WHERE difficulte_id = {self.diff}")
        self.liste_questions = self.cursor.fetchall()
        # réinitialise les variables pour démarrer la partie
        self.max_index = 39
        self.question_i = 0
        self.next_question()
        self.timer.reset()
        # reset scores
        self.scores = [0, 0]
        # choisit un background au hasard parmis les couleurs dispos
        # et change la couleur des éléments en fonction
        self.background_color = random.choice(self.possible_colors)
        self.ingame_img = pygame.image.load(f"img/background/questions/fond_{self.background_color}.png")
        self.timer.change_color(self.background_color)
        for b in self.answers_buttons:
            b.change_color(self.background_color)
        self.back_button.change_color(self.background_color)

    def end(self):
        #send scores
        self.app.scores.set_scores((self.nom_joueurs[0], self.scores[0]), (self.nom_joueurs[1], self.scores[1]))
        self.app.scores.set_scores_db()
        self.app.scores.get_scores_db()

        self.app.set_state('GameOver')
        self.reset()
        pass
