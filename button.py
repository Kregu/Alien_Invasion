import pygame.font

class Button():
    def __init__(self, ai_settings, screen, msg):
        """ initialise button attribute """
        self.screen = screen
        self.screen_rect = screen.get_rect()

        # setup size and properties
        self.width, self.height = 200, 50
        self.button_color = (130, 200, 150)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        # build object rect button and alignment on center
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # button message create only once
        self.prep_msg(msg)

    def prep_msg(self, msg):
        """ transform msg to rect and alignment text """
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        """ display empty button and output message """
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)



