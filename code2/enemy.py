import pygame

class Pikachu():
    def __init__(self, screen):
        """Initialize the player and set its starting position."""
        self.screen = screen
        # Load the ship image and get its rect.
        self.image = pygame.image.load('images/pikachu.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        # Start each new ship at the bottom center of the screen.
        self.rect.right = self.screen_rect.right
        self.rect.centery = self.screen_rect.centery
        #Define initial stats
        self.health = 10
        self.attack = 1
        self.armour = 2
        self.magicDamage = 5
    def blitme(self):
        """Draw the player at its current location."""
        self.screen.blit(self.image, self.rect)

class johnCena():
    def __init__(self, screen):
        """Initialize the player and set its starting position."""
        self.screen = screen
        # Load the ship image and get its rect.
        self.image = pygame.image.load('images/johnCena.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        # Start each new ship at the bottom center of the screen.
        self.rect.right = self.screen_rect.right
        self.rect.centery = self.screen_rect.centery
        #Define initial stats
        self.health = 10
        self.attack = 1
        self.armour = 2
        self.magicDamage = 5
    def blitme(self):
        """Draw the player at its current location."""
        self.screen.blit(self.image, self.rect)

