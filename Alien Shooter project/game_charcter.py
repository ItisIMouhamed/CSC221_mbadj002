import pygame

# TIY 12-2 (Game Character)
class Game_Character:
    '''A class to manage the new character'''

    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Load the new game character image
        self.image = pygame.image.load('images/peguin.bmp')
        self.rect = self.image.get_rect()

        # Start new game charcter at the center of screen
        self.rect.center = self.screen_rect.center

    def blitme(self):
        '''Draw the ship at its current location'''
        self.screen.blit(self.image, self.rect)