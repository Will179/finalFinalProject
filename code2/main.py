"""
Final Project Take 2:
Restarted in final week, went off alien invasion template from textbook
ran into problem generating bullets, unable to fix the issue.


"""




import pygame
import sys
from settings import Settings
from player import Player
from enemy import *
import gameFunctions as gf
from pygame.sprite import Group
from alien import Alien
from game_stats import GameStats

def run_game():
    # Initialize pygame, settings, and screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Dungeon Fighter")

    # Create an instance to store game statistics.
    stats = GameStats(ai_settings)

    #create a player
    player = Player(ai_settings, screen)
    # Make a group to store bullets in. u
    bullets = Group()
    #Make a group to store Aliens
    aliens = Group()

    # Create the fleet of aliens. v
    gf.create_fleet(ai_settings, screen, player, aliens)

    # Start the main loop for the game.
    while True:
        #gf.start(player, enemy)
        gf.check_events(ai_settings, screen, player, bullets)
        if stats.game_active:
            player.update()
            gf.update_bullets(ai_settings, screen, player, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, player, aliens, bullets)
        gf.update_screen(ai_settings, screen, player, aliens, bullets)

        # Get rid of bullets that have disappeared. u
        for bullet in bullets.copy():
            if bullet.rect.bottom <= 0:
                bullets.remove(bullet)
                print(len(bullets))


run_game()

