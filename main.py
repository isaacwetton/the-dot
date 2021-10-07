# Import used modules
import math

# Import functions and classes from other modules within project
from menusprites import *

# Initialise pygame
pygame.init()

# Define any colours used
GREY = (85, 85, 85)
DARK_GREY = (50, 50, 50)
WHITE = (255, 255, 255)

# Create pi constant from math
PI = math.pi

# Create pygame info object
pygameInfo = pygame.display.Info()
screen_x = pygameInfo.current_w
screen_y = pygameInfo.current_h

# Create fullscreen game window
# screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
screen = pygame.display.set_mode((screen_x, screen_y))

# Set window title
pygame.display.set_caption("The Dot")

# Initialise quit condition
main_menu = True
finished = False

# Create clock
clock = pygame.time.Clock()

# Create sprite groups
main_menu_list = pygame.sprite.Group()

# Create main menu sprites
title = MainMenuTitle(screen_x * 0.3,
                      screen_y * 0.2,
                      (int((screen_x * 0.4) // 1), int((screen_y * 0.35) // 1)))
main_menu_list.add(title)

# --- MAIN MENU LOOP ---

while main_menu:
    # Event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            main_menu = False
            finished = True

    # Clear the screen to GREY with DARK_GREY border
    screen.fill(GREY)
    pygame.draw.rect(screen, DARK_GREY, [0, 0, pygameInfo.current_w, pygameInfo.current_h], 50)
    main_menu_list.draw(screen)
    pygame.display.flip()

    # Limit game to 60fps
    clock.tick(60)

# --- MAIN PROGRAM LOOP ---

while not finished:

    # Event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

    # Clear the screen to GREY with DARK_GREY border
    screen.fill(GREY)
    pygame.draw.rect(screen, DARK_GREY, [0, 0, pygameInfo.current_w, pygameInfo.current_h], 50)
    pygame.display.flip()

    # Limit game to 60fps
    clock.tick(60)

# Quit the program when the main game loop is exited
pygame.quit()
quit()
