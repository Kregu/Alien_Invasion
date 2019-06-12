import pygame
from settings import Settings
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
    play_button = Button(ai_settings, screen, "(P)lay")

    # create ship
    ship = Ship(ai_settings, screen)

    # create bullets group
    bullets = pygame.sprite.Group()

    # create alien group
    aliens = pygame.sprite.Group()

    # create alien fleet
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # music
    file_music = "music/240376__edtijo__happy-8bit-pixel-adenture.ogg"
    pygame.mixer.music.load(file_music)
    pygame.mixer.music.play(-1)

    # sounds
    shoot_sound = pygame.mixer.Sound("music/151022__bubaproducer__laser-shot-silenced.wav")
    boom_sound = pygame.mixer.Sound("music/boom.wav")

    # result
    file3 = "result.txt"


    # create instances of GameStats and Scoreboard
    stats = GameStats(ai_settings)
    stats.high_score = gf.load_result(file3)
    sb = Scoreboard(ai_settings, screen, stats)

    # RUN GAME
    while True:
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets, shoot_sound, file3)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets, boom_sound)
            gf.update_aliens(ai_settings, stats, sb, screen, ship, aliens, bullets, boom_sound)
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)


run_game()
