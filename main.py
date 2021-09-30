# Import used modules
import pygame
import math

# Initialise pygame
pygame.init()

# Define any colours used
DARK_GREY = (85, 85, 85)
WHITE = (255, 255, 255)

# Create pi constant from math
PI = math.pi

# Create pygame info object
pygameInfo = pygame.display.Info()

# Create fullscreen game window
# screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
screen = pygame.display.set_mode((pygameInfo.current_w, pygameInfo.current_h))

# Set window title
pygame.display.set_caption("The Dot")

# Initialise quit condition
finished = False

# Create clock
clock = pygame.time.Clock()

# --- MAIN PROGRAM LOOP ---

while not finished:

    # Event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

    # Clear the screen to DARK_GREY
    screen.fill(DARK_GREY)
    
    pygame.display.flip()

    # Limit game to 60fps
    clock.tick(60)

pygame.quit()
quit()
