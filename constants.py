import pygame

# Win size
WIN_SIZE = (1280,720)
WIN_X = 1280
WIN_Y = 720

# Game values
max_points = 20

# coords
question_number_pos = (180,215)
question_title_pos = (110,280)
start_text_pos = (WIN_X-225, 480)
quit_text_pos = (WIN_X-200, 22)

# images



# fonts
pygame.font.init()
font_karmatic = pygame.font.Font("fonts/ka1.ttf", 30)
font_lcd = pygame.font.Font("fonts/jd_lcd_rounded.ttf", 40)
font_pixelop = pygame.font.Font("fonts/PixelOperator.ttf", 36)
font_pixelop8 = pygame.font.Font("fonts/PixelOperator8.ttf", 20)
font_pixelop8small = pygame.font.Font("fonts/PixelOperator8.ttf", 12)
font_symtext = pygame.font.Font("fonts/Symtext.ttf", 32)
font_kemco = pygame.font.Font("fonts/Kemco_Pixel_Bold.ttf", 32)

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
        'Dark' : "#441300",
        'Mid' : "#6b0a00",
        'Light' : "#c49d99"
    },
    'Purple' : {
        'Dark' : "#441300",
        'Mid' : "#6b0a00",
        'Light' : "#c49d99"
    },
}

color_index = {
    0 : 'Red',
    1 : 'Blue',
    2 : 'Green',
}

# functions
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

