# Import used modules
import pygame


class MainMenuTitle(pygame.sprite.Sprite):
    """This is the sprite for the title text on the main menu"""

    def __init__(self):
        """Constructor.... """

        # Call pygame.sprite.Sprite constructor
        super().__init__()

        # Load the main menu image and corresponding rectangle dimensions
        self.image = pygame.image.load("TheDotTitle.png").convert()
        self.rect = self.image.get_rect()
