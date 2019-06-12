import sys
import pygame
import json
from time import sleep
from bullet import Bullet
from alien import Alien


def check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets, shoot_sound, file3):
    """process key down and mouse events"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            save_result(stats, file3)
            sys.exit()

        if event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, stats, sb, ship, aliens, bullets, shoot_sound, file3)

        if event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets, mouse_x, mouse_y)


def check_play_button(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets, mouse_x, mouse_y):
    """ run new game when by click on play button """
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked:
        # start new game
        start_game(ai_settings, screen, stats, sb, ship, aliens, bullets)


def start_game(ai_settings, screen, stats, sb, ship, aliens, bullets):
    """ start new game"""
    if not stats.game_active:

        # hide mouse
        pygame.mouse.set_visible(False)
        # reset game settings
        ai_settings.initialize_dynamic_settings()
        # reset game statistics
        stats.reset_stats()
        stats.game_active = True

        # reset scores and level images
        sb.prep_score()
        sb.prep_high_score()
        sb.prep_level()
        sb.prep_ships()

        # clear aliens and bullets
        aliens.empty()
        bullets.empty()

        # create new fleet and centered ship
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()


def check_keydown_events(event, ai_settings, screen, stats, sb, ship, aliens, bullets, shoot_sound, file3):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True

    elif event.key == pygame.K_LEFT:
        ship.moving_left = True

    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, stats, ship, bullets, shoot_sound)

    elif event.key == pygame.K_q or pygame.K_ESCAPE:
        save_result(stats, file3)
        sys.exit()

    elif event.key == pygame.K_p:
        start_game(ai_settings, screen, stats, sb, ship, aliens, bullets)


def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button):
    """fill display every iteration"""
    screen.fill(ai_settings.bg_color)

    # all bullets draw behind aliens ships
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    ship.blitme()

    aliens.draw(screen)

    # display score
    sb.show_score()

    # display Play Button only when game is inactive
    if not stats.game_active:
        play_button.draw_button()

    # view last screen
    pygame.display.flip()


def update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets, boom_sound):
    """update bullets position and remove old bullets"""
    # update position

    bullets.update()
    # remove bullets outside the screen
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship, aliens, bullets, boom_sound)


def check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship, aliens, bullets, boom_sound):
    """ respond to bullet-alien collisions """
    # check bullets hit the aliens.
    # when collisions remove bullets and aliens

    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if collisions:
        boom_sound.play()
        for aliens in collisions.values():
            stats.score += ai_settings.alien_points * len(aliens)
        sb.prep_score()
        check_high_score(stats, sb)


    if len(aliens) == 0:
        # if all aliens are destroyed, remove all bullets and create new fleet and start new level
        bullets.empty()
        ai_settings.increase_speed()
        create_fleet(ai_settings, screen, ship, aliens)
        # level up
        stats.level += 1
        sb.prep_level()


def fire_bullet(ai_settings, screen, stats, ship, bullets, shoot_sound):
    ''' fire bullet if max bullet is not reach'''
    # create new bullet and insert it to group bullets
    if len(bullets) < ai_settings.bullets_allowed and stats.game_active:
        shoot_sound.play()
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


def create_fleet(ai_settings, screen, ship, aliens):
    """create alien fleet"""
    # create alien and calculate many in row
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_numbere_alien_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)

    # create aliens fleet
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings, screen, aliens, alien_number, row_number)


def get_numbere_alien_x(ai_settings, alien_width):
    """ calculate alien in row """
    # interval between alien equivalently one alien
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x


def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    # create a alien and put it in row
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien_height = alien.rect.height
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien_height + 1.4 * alien_height * row_number + 10
    aliens.add(alien)


def get_number_rows(ai_settings, ship_hight, alien_height):
    """calclulate number aliens rows"""
    available_space_y = (ai_settings.screen_height - 3 * alien_height - 3 * ship_hight)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows


def update_aliens(ai_settings, stats, sb, screen, ship, aliens, bullets, boom_sound):
    """ check edges and update aliens position in all fleet"""
    check_fleet_edges(ai_settings, aliens)
    aliens.update()
    # check collisions alien - ship
    if pygame.sprite.spritecollideany(ship, aliens):
        boom_sound.play()
        ship_hit(ai_settings, stats, sb, screen, ship, aliens, bullets)
    # check aliens come to bottom screen
    check_aliens_bottom(ai_settings, stats, sb, screen, ship, aliens, bullets)


def check_fleet_edges(ai_settings, aliens):
    """ reacts to alien come edges """
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break


def change_fleet_direction(ai_settings, aliens):
    """ moves fleet down and chandge direction """
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1


def ship_hit(ai_settings, stats, sb, screen, ship, aliens, bullets):
    """ react to ship - alien collision """
    # decrease ship left
    if stats.ship_left > 0:
        stats.ship_left -= 1
        # clear groups aliens and bullets
        aliens.empty()
        bullets.empty()
        sb.prep_ships()
        # create new fleet and centered ship
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()
        # pause
        sleep(0.5)
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)


def check_aliens_bottom(ai_settings, stats, sb, screen, ship, aliens, bullets):
    """ check aliens come to bottom screen """
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            # same as ship hit
            ship_hit(ai_settings, stats, sb, screen, ship, aliens, bullets)
            break

def play_sound(sound_file):
    """ play any sound """
    #winsound.PlaySound(sound_file, winsound.SND_ASYNC)
    pygame.mixer.Sound(sound_file)

def check_high_score(stats, sb):
    """ check new record score """
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()

def save_result(stats, file3):
    file_result = open(file3, mode='w')
    json.dump(stats.high_score, file_result)
    file_result.close()

def load_result(file3):
    try:
        file_result = open(file3, mode='r')
    except FileNotFoundError:
        print("File with previous result is not found.")
        return 0
    else:
        return json.load(file_result)







