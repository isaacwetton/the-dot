# Import used modules
import pygame

# Define used colours
WHITE = (255, 255, 255)


class MainMenuTitle(pygame.sprite.Sprite):
    """This is the sprite for the title text on the main menu"""

    def __init__(self, xpos, ypos, size):
        """Constructor.... """

        # Call pygame.sprite.Sprite constructor
        super().__init__()

        # Load the main menu image and corresponding rectangle dimensions
        self.image = pygame.image.load("TheDotTitle.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, size)
        self.rect = self.image.get_rect()
        self.rect.x = xpos
        self.rect.y = ypos
