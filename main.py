# Import used modules
import pygame
import math

# Initialise pygame
pygame.init()

# Define any colours used

# Create pi constant from math
PI = math.pi

# Create fullscreen game window
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

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

    # Limit game to 144fps
    clock.tick(144)
