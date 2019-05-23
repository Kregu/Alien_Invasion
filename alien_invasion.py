import pygame

from settings import Settings
from pygame.sprite import Group
from game_stats import GameStats
from ship import Ship
from button import Button
from scoreboard import Scoreboard

import game_functions as gf


def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # create play button
    play_button = Button(ai_settings, screen, "Play")

    # create an instance for storing statistics
    stats = GameStats(ai_settings)

    # create ship
    ship = Ship(ai_settings, screen)

    # create alien
    #alien = Alien(ai_settings, screen)

    # create bullets group
    bullets = Group()

    # create alien group
    aliens = Group()

    # create alien fleet
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # music
    file1 = "music/240376__edtijo__happy-8bit-pixel-adenture.wav"
    file2 = "music/151022__bubaproducer__laser-shot-silenced.wav"

    gf.play_sound(file1)

    # create instances of GameStats and Scoreboard
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)


    # RUN GAME
    while True:
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets, file2)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)


run_game()
