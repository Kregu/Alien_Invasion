import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """class for bullets control"""

    def __init__(self, ai_settings, screen, ship):
        '''create a bullet in the current ship location'''
        super(Bullet, self).__init__()
        self.screen = screen

        # create bullet in 0,0 position and move to the ship position
        self.rect = pygame.Rect(0,0,ai_settings.bullet_width, ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # bullet position in float format
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        """move bullet up"""

        # update bullet position in float format
        self.y -= self.speed_factor

        # update bullet position
        self.rect.y = self.y

    def draw_bullet(self):
        """ draw bullet on the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)





