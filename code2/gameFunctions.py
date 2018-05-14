import sys
import pygame
import random
import math

def check_events():
    """Respond to keypresses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

def update_screen(ai_settings, screen, player, enemy):
    """Update images on the screen and flip to the new screen."""
    # Redraw the screen during each pass through the loop.
    screen.fill(ai_settings.bg_color)
    player.blitme()
    enemy.blitme()
    # Make the most recently drawn screen visible.
    pygame.display.flip()

def start(player, enemy):
    print("Welcome to Dungeon Fighter!")
    print("your goal is to clear as many floors as possible,")
    print("On your quest you will face monsters and traps, but also some awesome loot!")
    print("You can type move to go to the next room, items to see your inventory or use a consumable item"
          "or inventory to equip weapons")
    a = input("Are you ready to play?")
    if a == "Yes":
        game(player, enemy)
    if a == "No":
        sys.exit()



def game(player, enemy):
    print("")
    choice = input("What do you want to do?")
    if choice == "attack":
        attack(player, enemy)
    if choice == "end game":
        sys.exit()

def attack(player, enemy):
    enemy.health = enemy.health - (player.attack/enemy.armour)
    print("")
    print("enemy's remaining health is: " + str(round(enemy.health)))
    if enemy.health > 0:
        enemyAttack(player, enemy)
    if enemy.health <= 0:
        newEnemy(player, enemy)

def enemyAttack(player, enemy):
    player.health = player.health - (enemy.attack/player.armour)
    print("")
    print("The enemy attacked you!")
    print("Your health is: " + str(round(player.health)))

def newEnemy(player, enemy):
    enemyNumber = random.randint(1,2)
    if enemyNumber == 1:
        print("A wild Pikachu Appeared")
        enemy.health = 10
        enemy.attack = 1
        enemy.armour = 2
        enemy.magicDamage = 5
    if enemyNumber == 2:
        print("A wild John Cena Approaches")
        enemy.health = 15
        enemy.attack = 2
        enemy.armour = 1.5
        enemy.magicDamage = 0




