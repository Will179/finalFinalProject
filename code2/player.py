import pygame

class Player():
    def __init__(self, screen):
        """Initialize the player and set its starting position."""
        self.screen = screen
        # Load the ship image and get its rect.
        self.image = pygame.image.load('images/Knight.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        # Start each new ship at the bottom center of the screen.
        self.rect.left = self.screen_rect.left
        self.rect.centery = self.screen_rect.centery
        #Define initial stats
        self.health = 100
        self.attack = 10
        self.armour = 5
        self.magicDamage = 15
    def blitme(self):
        """Draw the player at its current location."""
        self.screen.blit(self.image, self.rect)
