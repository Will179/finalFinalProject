import pygame
import sys
from settings import Settings
from player import Player
from enemy import *
import gameFunctions as gf



def run_game():
    # Initialize pygame, settings, and screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Dungeon Fighter")
    #create a player
    player = Player(screen)
    enemy = Pikachu(screen)
    # Start the main loop for the game.
    while True:
        gf.start(player, enemy)
    #gf.check_events()
    #gf.update_screen(ai_settings, screen, player, enemy)
run_game()

