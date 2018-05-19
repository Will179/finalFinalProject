import sys
import pygame
import random
from bullet import Bullet
from alien import Alien
from time import sleep


def check_events(ai_settings, screen, stats, play_button, player, aliens, bullets):
    """Respond to keypresses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, screen, stats, play_button, player, aliens, bullets, mouse_x, mouse_y)
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, player, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, player)

def check_play_button(ai_settings, screen, stats, play_button, player, aliens, bullets, mouse_x, mouse_y):
    """Start a new game when the player clicks Play."""
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        # Reset the game settings.
        ai_settings.initialize_dynamic_settings()
        # Hide the mouse cursor.
        pygame.mouse.set_visible(False)
        # Reset the game statistics.
        stats.reset_stats()
        stats.game_active = True
        # Empty the list of aliens and bullets. v
        aliens.empty()
        bullets.empty()
        # Create a new fleet and center the ship. w
        create_fleet(ai_settings, screen, player, aliens)
        player.center_player()


def check_keydown_events(event, ai_settings, screen, player, bullets):
    """Respond to keypresses."""
    if event.key == pygame.K_RIGHT:
        player.moving_right = True
    elif event.key == pygame.K_LEFT:
        player.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, player, bullets)
    elif event.key == pygame.K_q:
        sys.exit()


def check_keyup_events(event, player):
    """Respond to key releases."""
    if event.key == pygame.K_RIGHT:
        player.moving_right = False
    elif event.key == pygame.K_LEFT:
        player.moving_left = False


def fire_bullet(ai_settings, screen, player, bullets):
    """Fire a bullet if limit not reached yet."""
    # Create a new bullet and add it to the bullets group.
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, player)
        bullets.add(new_bullet)

def update_bullets(ai_settings, screen, player, aliens, bullets):
    """"Update position of bullets and get rid of old bullets."""
    # Update bullet positions.
    bullets.update()
    # Get rid of bullets that have disappeared. u
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    # Check for any bullets that have hit aliens.
    #  If so, get rid of the bullet and the alien.
    check_bullet_alien_collisions(ai_settings, screen, player, aliens, bullets)

def check_bullet_alien_collisions(ai_settings, screen, player, aliens, bullets):
    """Respond to bullet-alien collisions."""
    # Remove any bullets and aliens that have collided.
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)

    if len(aliens) == 0:
        # Destroy existing bullets, speed up game, and create new fleet.
        bullets.empty()
        ai_settings.increase_speed()
        create_fleet(ai_settings, screen, player, aliens)


def update_screen(ai_settings, screen, stats, player, aliens, bullets, play_button):
    """Update images on the screen and flip to the new screen."""
    # Redraw the screen during each pass through the loop.
    screen.fill(ai_settings.bg_color)
    # Redraw all bullets behind ship and aliens. y
    for bullet in bullets.sprites():
        bullet.draw_bullet()
        # print("Bullet Drawn")
    player.blitme()
    aliens.draw(screen)

    # Draw the play button if the game is inactive.
    if not stats.game_active:
        play_button.draw_button()

    # Make the most recently drawn screen visible.
    pygame.display.flip()

def get_number_aliens_x(ai_settings, alien_width):
    """Determine the number of aliens that fit in a row."""
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x


def get_number_rows(ai_settings, player_height, alien_height):
    """Determine the number of rows of aliens that fit on the screen."""
    available_space_y = (ai_settings.screen_height - (3 * alien_height) - player_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows

def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    """Create an alien and place it in the row."""
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)

def create_fleet(ai_settings, screen, player, aliens):
    """Create a full fleet of aliens."""
    # Create an alien and find the number of aliens in a row.
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, player.rect.height, alien.rect.height)
    # Create the first row of aliens.
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings, screen, aliens, alien_number, row_number)

def check_fleet_edges(ai_settings, aliens):
    """Respond appropriately if any aliens have reached an edge."""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break

def change_fleet_direction(ai_settings, aliens):
    """Drop the entire fleet and change the fleet's direction."""
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1


def update_aliens(ai_settings, stats, screen, player, aliens, bullets):
    """    Check if the fleet is at an edge, and then update the postions of all aliens in the fleet.    """
    check_fleet_edges(ai_settings, aliens)
    aliens.update()
    # Look for alien-ship collisions.
    if pygame.sprite.spritecollideany(player, aliens):
        player_hit(ai_settings, stats, screen, player, aliens, bullets)
    # Look for aliens hitting the bottom of the screen. v
    check_aliens_bottom(ai_settings, stats, screen, player, aliens, bullets)


def player_hit(ai_settings, stats, screen, player, aliens, bullets):
    if stats.players_left > 0:
        """Respond to ship being hit by alien."""
        # Decrement ships_left.
        stats.players_left -= 1
        # Empty the list of aliens and bullets.
        aliens.empty()
        bullets.empty()
        # Create a new fleet and center the ship.
        create_fleet(ai_settings, screen, player, aliens)
        player.center_player()
        # Pause.
        sleep(0.5)
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)


def check_aliens_bottom(ai_settings, stats, screen, player, aliens, bullets):
    """Check if any aliens have reached the bottom of the screen."""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            # Treat this the same as if the ship got hit.
            player_hit(ai_settings, stats, screen, player, aliens, bullets)
            break


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








