class Settings:
    """ Class for store game settings """

    def __init__(self):
        """ initialize static game settings """
        # screen parameters
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0, 0, 102)

        # ship parameters
        self.ship_width = 48
        self.ship_height = 48
        self.ship_limit = 2

        # bullets
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 255, 0, 0
        self.bullets_allowed = 10

        # alien
        self.alien_width = 40
        self.alien_height = 40
        self.fleet_drop_speed = 10

        # increase game speed
        self.speedup_scale = 1.1

        # increase aliens cost
        self.score_scale = 1.5

        # initialize dynamic settings
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """ initialize settings changed during the game """
        self.ship_speed_factor = 1
        self.bullet_speed_factor = 2
        self.alien_speed_factor = 0.5

        # fleet_direction: 1 = right, -1 = left
        self.fleet_direction = 1

        # calculate.score
        self.alien_points = 50


    def increase_speed(self):
        """ increase game speed and aliens cost """
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)

