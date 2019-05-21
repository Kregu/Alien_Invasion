class GameStats():
    """collect game statistics"""

    def __init__(self, ai_settings):
        """initialize statistics"""
        self.ai_settings = ai_settings
        self.reset_stats()
        # run Alien Invasion in active state
        self.game_active = False

    def reset_stats(self):
        """initializes statistics changing during the game"""
        self.ship_left = self.ai_settings.ship_limit
        self.score = 0




