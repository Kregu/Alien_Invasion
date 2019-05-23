class GameStats():
    """collect game statistics"""

    def __init__(self, ai_settings):
        """initialize statistics"""
        self.ai_settings = ai_settings
        self.reset_stats()
        # run Alien Invasion in active state
        self.game_active = False

        # record, do not reset
        self.high_score = 0

    def reset_stats(self):
        """initializes statistics changing during the game"""
        self.ship_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1




