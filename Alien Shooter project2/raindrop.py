import pygame
from pygame.sprite import Sprite

class Raindrop(Sprite):
    """A class to represent a single raindrop in the fleet."""

    def __init__(self, ai_game):
        """Initialize the star and set its starting position."""
        super().__init__()
        self.screen = ai_game.screen

        # Load the star image and set its rect attribute

        #self.image = pygame.image.load('images/star.png')
        self.image = pygame.image.load('images/raindrop.png')
        self.rect = self.image.get_rect()

        # Start each new star near the top of the screen.

        self.rect.x = 100#self.rect.width
        self.rect.y = 100#self.rect.height

        # Store the aliens exact horizontal position.
        self.x = float(self.rect.x)


