import pygame

# Win size
WIN_SIZE = (1280,720)
WIN_X = 1280
WIN_Y = 720

# Game values
max_points = 150
min_points = 30
time_per_question = 20

# coords
pos_question_number = (180,215)
pos_question_title = (110,280)
pos_start_text = (WIN_X-225, 480)
pos_quit_text = (WIN_X-200, 22)

pos_menu_quit = (1036,40)
pos_menu_quit_text = (1075,60)
pos_menu_start = (1036,415)
pos_menu_start_text = (1088,435)
pos_menu_regle = (1036,500)
pos_menu_regle_text = (1078,522)
pos_menu_score = (1036,585)
pos_menu_score_text = (1076,607)

pos_options_start = (1036,40)
pos_options_start_text = (1088,61)
pos_options_retour = (55,40)
pos_options_retour_text = (98,61)
pos_options_1joueur = (240,250)
pos_options_1joueur_text = (316,275)
pos_options_2joueur = (760,250)
pos_options_2joueur_text = (826,275)
pos_options_nom_1 = (240,350)
pos_options_nom_2 = (760,350)
pos_options_easy = (180,590)
pos_options_easy_text = (287,613)
pos_options_medium = (500,590)
pos_options_medium_text = (596,613)
pos_options_hard = (820,590)
pos_options_hard_text = (885,613)
pos_options_bg_text_1 = (109,141)
pos_options_bg_text_2 = (226,473)
pos_options_icon1 = (140,245)
pos_options_icon2 = (660,245)


pos_game_nom_joueur_1 = (1100, 164)
pos_game_nom_joueur_2 = (1100, 275)
pos_game_score_1 = (1100, 189)
pos_game_score_2 = (1100, 300)
pos_game_icon_1 = (1000, 150)
pos_game_icon_2 = (1000, 260)

pos_gameover_retour = (55,40)
pos_gameover_rejouer = (545,40)
pos_gameover_scores = (1036,40)
pos_gameover_quitter = (55,620)
pos_gameover_retour_text = (98,60)
pos_gameover_rejouer_text = (579,60)
pos_gameover_scores_text = (1076,60)
pos_gameover_quitter_text = (96,640)

rect_rules_border = pygame.Rect(WIN_X/6, WIN_Y/8, WIN_X - WIN_X/3, WIN_Y*0.75)
rect_rules_inside = pygame.Rect(WIN_X/6 +10, WIN_Y/8 +10, WIN_X - WIN_X/3 -20, WIN_Y*0.75 -20)
pos_rules_text = (WIN_X/6 + 20,WIN_Y/8 + 30)
pos_rules_margin = 17.5
pos_rules_close = (WIN_X/6 -8, WIN_Y/8 - 8)


# images
img_quizz_icon = pygame.image.load('img/icon_quizz.ico')
img_name_input = pygame.image.load("img/boutons/menu/bloc_text.png")
img_menu_background = pygame.image.load("img/background/menus/background.png")
img_menu_start = pygame.image.load("img/boutons/menu/menu_nopush.png")
img_menu_start_push = pygame.image.load("img/boutons/menu/menu_push.png")
img_rules_close = pygame.image.load("img/boutons/menu/fermer.png")
img_facile = pygame.image.load("img/boutons/menu/noob_nopush.png")
img_facile_push = pygame.image.load("img/boutons/menu/noob_push.png")
img_moyen = pygame.image.load("img/boutons/menu/gamer_nopush.png")
img_moyen_push = pygame.image.load("img/boutons/menu/gamer_push.png")
img_difficile = pygame.image.load("img/boutons/menu/progamer_nopush.png")
img_difficile_push = pygame.image.load("img/boutons/menu/progamer_push.png")
img_reponse = pygame.image.load("img/boutons/questions/rep_nopush_blue.png")
img_options_background = pygame.image.load("img/background/menus/menu_parametres.png")
img_reponse_bleu_push = pygame.image.load("img/boutons/questions/rep_push_blue.png")
img_background_gameover = pygame.image.load("img/background/menus/menu_gameover.png")
img_gameover_retour_push = pygame.image.load("img/boutons/menu/go_jaune_push.png")
img_gameover_retour_nopush = pygame.image.load("img/boutons/menu/go_jaune_nopush.png")
img_gameover_rejouer_push = pygame.image.load("img/boutons/menu/go_bleu_push.png")
img_gameover_rejouer_nopush = pygame.image.load("img/boutons/menu/go_bleu_nopush.png")
img_gameover_scores_push = pygame.image.load("img/boutons/menu/go_bleuc_push.png")
img_gameover_scores_nopush = pygame.image.load("img/boutons/menu/go_bleuc_nopush.png")
img_gameover_quitter_push = pygame.image.load("img/boutons/menu/go_orange_push.png")
img_gameover_quitter_nopush = pygame.image.load("img/boutons/menu/go_orange_nopush.png")
img_options_icones = [pygame.image.load("img/joueurs/joueur1.png"),
                      pygame.image.load("img/joueurs/joueur2.png"),
                      pygame.image.load("img/joueurs/joueur3.png"),
                      pygame.image.load("img/joueurs/joueur4.png"),
                      pygame.image.load("img/joueurs/joueur5.png"),
                      pygame.image.load("img/joueurs/joueur6.png"),
                      pygame.image.load("img/joueurs/joueur7.png"),
                      pygame.image.load("img/joueurs/joueur8.png"),
                      pygame.image.load("img/joueurs/joueur9.png"),
                      pygame.image.load("img/joueurs/joueur10.png"),
                      pygame.image.load("img/joueurs/joueur11.png"),
                      pygame.image.load("img/joueurs/joueur12.png")
                      ]


# fonts
pygame.font.init()
font_karmatic20 = pygame.font.Font("fonts/ka1.ttf", 20)
font_karmatic30 = pygame.font.Font("fonts/ka1.ttf", 30)
font_karmatic50 = pygame.font.Font("fonts/ka1.ttf", 50)
font_lcd = pygame.font.Font("fonts/jd_lcd_rounded.ttf", 40)
font_pixelop = pygame.font.Font("fonts/PixelOperator.ttf", 36)
font_pixelop8 = pygame.font.Font("fonts/PixelOperator8.ttf", 20)
font_pixelop8small = pygame.font.Font("fonts/PixelOperator8.ttf", 12)
font_symtext = pygame.font.Font("fonts/Symtext.ttf", 32)
font_kemco = pygame.font.Font("fonts/Kemco_Pixel_Bold.ttf", 26)

# colors
D_GREEN = "#004428"
GREEN = "#006b2c"
L_GREEN = "#99c4ab"
D_BLUE = "#001964"
BLUE = "#00418a"
L_BLUE = "#99b3d0"
D_CYAN = "#002b3f"
CYAN = "#00616b"
L_CYAN = "#99c0c4"
D_YELLOW = "#354400"
YELLOW = "#686b00"
L_YELLOW = "#c3c499"
D_GREY = "#222222"
GREY = "#353535"
L_GREY = "#c2b2b5"
D_ORANGE = "#3f2c00"
ORANGE = "#6b3300"
L_ORANGE = "#c4ad99"
D_RED = "#441300"
RED = "#6b0a00"
L_RED = "#c49d99"
D_PURPLE = "#44003f"
PURPLE = "#5e006b"
L_PURPLE = "#bf99c4"
'''
TO DO v
'''
colors = {
    'Red' : {
        'Dark' : "#441300",
        'Mid' : "#6b0a00",
        'Light' : "#c49d99"
    },
    'Blue' : {
        'Dark' : "#001964",
        'Mid' : "#00418a",
        'Light' : "#99b3d0"
    },
    'Green' : {
        'Dark' : "#004428",
        'Mid' : "#006b2c",
        'Light' : "#99c4ab"
    },
    'Yellow' : {
        'Dark' : "#354400",
        'Mid' : "#686b00",
        'Light' : "#c3c499"
    },
    'Purple' : {
        'Dark' : "#44003f",
        'Mid' : "#5e006b",
        'Light' : "#bf99c4"
    },
    'Grey' : {
        'Dark' : "#222222",
        'Mid' : "#353535",
        'Light' : "#c2b2b5"
    },
    'Cyan' : {
        'Dark' : "#002b3f",
        'Mid' : "#00616b",
        'Light' : "#99c0c4"
    },
    'Orange' : {
        'Dark' : "#3f2c00",
        'Mid' : "#6b3300",
        'Light' : "#c4ad99"
    },
}


# functions

# affiche du texte, avec retour à la ligne automatique
def blit_text(surface, text, pos, max_width, font, color=pygame.Color('black')):
    words = [word.split(' ') for word in text.splitlines()]  # 2D array where each row is a list of words.
    space = font.size(' ')[0]  # The width of a space.
    x, y = pos
    for line in words:
        for word in line:
            word_surface = font.render(word, 0, color)
            word_width, word_height = word_surface.get_size()
            if x + word_width >= max_width:
                x = pos[0]  # Reset the x.
                y += word_height  # Start on new row.
            surface.blit(word_surface, (x, y))
            x += word_width + space
        x = pos[0]  # Reset the x.

