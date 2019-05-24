import pygame
from pygame.sprite import Sprite

class Ship(Sprite):

    def __init__(self, ai_settings, screen):
        """ship initialization and start point the ship"""

        super(Ship, self).__init__()

        self.screen = screen
        self.ai_settings = ai_settings

        """load ship and get rect"""

        self.image = pygame.image.load('images/ship.png')
        self.image = pygame.transform.scale(self.image, (ai_settings.ship_width, ai_settings.ship_height))
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # each new ship on down border
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # save float coordinate ship center
        self.center = float(self.rect.centerx)

        # moving flag
        self.moving_right = False
        self.moving_left = False



    def update(self):
        # update ship position by flag
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > self.screen_rect.left:
            self.center -= self.ai_settings.ship_speed_factor

        # update rect by self.center
        self.rect.centerx = self.center

    def blitme(self):
        """drow ship"""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """ center ship on down edge """
        self.center = self.screen_rect.centerx


