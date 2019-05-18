import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    # One alien class

    def __init__(self, ai_settings, screen):
        """ Init alien and setup start position """

        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        # Load alien and set rect attribute

        self.image = pygame.image.load('images/alien.png')
        self.image = pygame.transform.scale(self.image, (ai_settings.alien_width, ai_settings.alien_height))

        self.rect = self.image.get_rect()

        # every new alien come in upper left angle screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # save alien precise position
        self.x = float(self.rect.x)

    def blitme(self):
        """ output alien in current location """
        self.screen.blit(self.image, self.rect)

    def update(self):
        """ move alien right or left"""
        self.x += self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction
        self.rect.x = self.x

    def check_edges(self):
        """ return True if alien near edge screen"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True





