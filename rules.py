import pygame
import constants as C

class Rules:
    def __init__(self, app):
        self.app = app
        self.screen = app.screen

        self.corners = 9

        self.texts =[
            "Bonjour jeune padawan !",
            "Bienvenue dans Game Quizz, le jeu qui teste tes connaissances sur le monde du jeu vidéo !",
            "Pour y jouer, rien de plus simple. Tout d’abord tu dois choisir le nombre de joueur et ",
            "ton/vos pseudo !",

            "Ensuite tu choisis ton niveau de difficulté : ",
            '    - vert étant le plus simple : "noob" ',
            '    - orange pour un niveau moyen :"gamer" ',
            '    - rouge : "pro-gamer", pour les gros malades qui ont passé plus d’heures à farmer ',
            '      sur Minecraft ces 10 dernières années que de temps IRL',

            "Les questions auxquelles tu vas devoir répondre correspondent au niveau de difficulté ",
            "choisi. Réfléchis bien ! ",

            'Il suffit ensuite d’appuyer sur le bouton "Start", et le jeu peut enfin commencer ! Enjoy !',
            "Lorsque la question apparaît, tu disposes de 15 secondes pour y répondre, en choisissant",
            "une des 4 réponses possibles. Attention: à chaque fois il n’y a qu’une seule bonne réponse!",
            "Si ta réponse est correcte, tu obtiendras alors des points. Attention cependant:",
            "plus tu prendras de temps à répondre moins tu auras de point (15 secondes = 150pts, 14",
            "secondes = 140pts, avec un minimum de 30 points).",
            "Si la réponse que tu as choisie est fausse, alors tu ne gagnes pas de points. ",
            'Si tu n’arrives pas à te décider dans le temps imparti et que tu n’as sélectionné aucune',
            'réponse, tu ne gagnes pas de points et on passe à la question suivante. ',
            'Dans tous les cas, une fois que tu as cliqué sur la réponse que tu penses être juste,',
            'la question suivante apparaît, et le jeu continue ainsi jusqu’à ce que chaque joueur',
            'soit arrivé à la fin de ses 10 questions. ',
            'Une fois que chaque joueur est arrivé à 10 questions, on passe au tableau des scores',
            'et vous pouvez donc comparer vos résultats, et éventuellement jouer à nouveau en',
            'appuyant sur le bouton rejouer ! ',
            '',
            'Que le jeu commence !',
        ]

    def draw(self):
        # draw outside rect
        pygame.draw.rect(self.screen, C.D_BLUE, C.rect_rules_border, 0,
                         self.corners)
        # draw inside rect
        pygame.draw.rect(self.screen, C.BLUE, C.rect_rules_inside, 0, self.corners)

        self.draw_text()

    def draw_text(self):
        for i,l in enumerate(self.texts):
            C.blit_text(self.screen, l, (C.pos_rules_text[0], C.pos_rules_text[1] + i*C.pos_rules_margin),
                        C.WIN_X - C.WIN_X/6, C.font_pixelop8small, 'white')