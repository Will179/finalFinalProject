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



def run_game():
    # Initialize pygame, settings, and screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Dungeon Fighter")
    #create a player
    player = Player(ai_settings, screen)
    # Make a group to store bullets in. u
    bullets = Group()
    # Start the main loop for the game.

    while True:
        #gf.start(player, enemy)
        gf.check_events(ai_settings, screen, player, bullets)
        player.update()
        bullets.update()
        gf.update_screen(ai_settings, screen, player, bullets)


run_game()

