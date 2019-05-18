class Settings:
    """Class for store game settings"""

    def __init__(self):
        # initialization game settings
        # screen parameters
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0, 0, 102)
        # ship parameters
        self.ship_width = 48
        self.ship_height = 48
        self.ship_speed_factor = 1
        self.ship_limit = 2

        # bullets
        self.bullet_speed_factor = 2
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 255, 0, 0
        self.bullets_allowed = 15

        # alien
        self.alien_width = 36
        self.alien_height = 36
        self.alien_speed_factor = 0.5
        self.fleet_drop_speed = 10

        # fleet_direction: 1 = right, -1 = left
        self.fleet_direction = 1
