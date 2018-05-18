import sys
import pygame
import random
from bullet import Bullet
import math

def check_events(ai_settings, screen, player, bullets):
    """Respond to keypresses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, player, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, player)
def check_keydown_events(event, ai_settings, screen, player, bullets):
    """Respond to keypresses."""
    if event.key == pygame.K_RIGHT:
        player.moving_right = True
    elif event.key == pygame.K_LEFT:
        player.moving_left = True
    elif event.key == pygame.K_SPACE:
        # Create a new bullet and add it to the bullets group.
        new_bullet = Bullet(ai_settings, screen, player)
        bullets.add(new_bullet)
        print("Bullet Created")


def check_keyup_events(event, player):
    """Respond to key releases."""
    if event.key == pygame.K_RIGHT:
        player.moving_right = False
    elif event.key == pygame.K_LEFT:
        player.moving_left = False


def fire_bullet(ai_settings, screen, player, bullets):
    """Fire a bullet if limit not reached yet."""
    # Create a new bullet and add it to the bullets group.
    new_bullet = Bullet(ai_settings, screen, player)
    bullets.add(new_bullet)
    print("Fired A bullet")

def update_bullets(bullets):
     """Update position of bullets and get rid of old bullets."""
     # Update bullet positions.
     bullets.update()
     # Get rid of bullets that have disappeared. u
     for bullet in bullets.copy():
         if bullet.rect.bottom <= 0:
             bullets.remove(bullet)


def update_screen(ai_settings, screen, player, bullets):
    """Update images on the screen and flip to the new screen."""
    # Redraw the screen during each pass through the loop.
    screen.fill(ai_settings.bg_color)
    # Redraw all bullets behind ship and aliens. y
    for bullet in bullets.sprites():
        bullet.draw_bullet()
        # print("Bullet Drawn")
    player.blitme()
    # Make the most recently drawn screen visible.
    pygame.display.flip()




def start(player, enemy):
    print("Welcome to Dungeon Fighter!")
    print("your goal is to clear as many floors as possible,")
    print("On your quest you will face monsters and traps, but also some awesome loot!")
    print("You can type move to go to the next room, items to see your inventory or use a consumable item"
          "or inventory to equip weapons")
    print("When asked questions, type Yes or No for that response")
    a = input("Are you ready to play?")
    if a == "Yes":
        game(player, enemy)
    if a == "No":
        sys.exit()



def game(player, enemy):
    print("")
    choice = input("What do you want to do?")
    if choice == "move forward":
        event = random.randint(1,2)
        if event == 1:
            newEnemy(player, enemy)
        if event == 2:
            fortnite(player,enemy)
    if choice == "end game":
        sys.exit()
    checkLevel(player, enemy)
    game(player,enemy)

def battle(player, enemy):
    print("")
    action = input("How do you wish to fight")
    if action == "attack":
        attack(player, enemy)
    battle(player, enemy)



def attack(player, enemy):
    enemy.health = enemy.health - (player.attack/enemy.armour)
    print("")
    print("enemy's remaining health is: " + str(round(enemy.health)))
    if enemy.health > 0:
        enemyAttack(player, enemy)
    if enemy.health <= 0:
        print("You killed the enemy and earned 10 exp!")
        player.exp += 10
        game(player, enemy)

def enemyAttack(player, enemy):
    player.health = player.health - (enemy.attack/player.armour)
    print("")
    print("The enemy attacked you!")
    print("Your health is: " + str(round(player.health)))
    battle(player,enemy)

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
    battle(player,enemy)

def fortnite(player, enemy):
    print("You find yourself at a strange portal")
    playFortnite = input("Do you wish to enter?")
    if playFortnite == "Yes":
        print("When you enter it you find yourself on a strange flying bus")
        print("You quickly realize that you are in a Fortnite game!")
        print("Sadly you realize you suck at Fornite, chances are you will die!")
        fortniteResult = random.randint(1,100)
        if fortniteResult == 100:
            print("")
            print("You somehow managed to win!")
            game(player, enemy)
            player.exp += 1000
        if fortniteResult < 100:
            print("")
            print("You lost the game and died, sorry")
            sys.exit()
    if playFortnite == "No":
        print("You chose not to play!")

def checkLevel(player, enemy):
    if player.exp >= player.expr:
        player.level += 1
        print("You leveled up to level " + str(player.level))
        player.exp = player.exp - player.expr
        player.expr = player.expr + player.level^2
        checkLevel(player, enemy)
    if player.exp < player.expr:
        game(player, enemy)








