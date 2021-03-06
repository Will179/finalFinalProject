"""
Final Project Take 2:
Restarted in final week, went off alien invasion template from textbook
ran into problem generating bullets, unable to fix the issue.
Since fixed bullets and made more progress on the Alien Invasion project


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
from button import Button
from scoreboard import Scoreboard

def run_game():
    # Initialize pygame, settings, and screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Dungeon Fighter")

    # Make the Play button.
    play_button = Button(ai_settings, screen, "Play")

    # Create an instance to store game statistics and create a scoreboard
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)

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
        sb = Scoreboard(ai_settings, screen, stats)
        #gf.start(player, enemy)
        gf.check_events(ai_settings, screen, stats, play_button, player, aliens, bullets)
        if stats.game_active:
            player.update()
            gf.update_bullets(ai_settings, screen, stats, sb, player, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, player, aliens, bullets)

        gf.update_screen(ai_settings, screen, stats, sb, player, aliens, bullets, play_button)

        # Get rid of bullets that have disappeared. u
        for bullet in bullets.copy():
            if bullet.rect.bottom <= 0:
                bullets.remove(bullet)
                print(len(bullets))


run_game()

