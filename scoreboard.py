import pygame.font

class Scoreboard():
    """ class for output game information's """
    def __init__(self, ai_settings, screen, stats):
        """ initialize score attributes """
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats

        # set font for displaying information
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        # create original screen
        self.prep_score()

    def prep_score(self):
        # convert score to graphic image
        score_str =  str(self.stats.score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.ai_settings.bg_color)

        # display score image on top right screen
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect - 20
        self.score_image.top = 20
