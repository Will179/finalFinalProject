import pygame

class Player():
    def __init__(self, ai_settings, screen):
        """Initialize the player and set its starting position."""
        self.screen = screen
        self.ai_settings = ai_settings
        # Load the ship image and get its rect.
        self.image = pygame.image.load('images/betterspaceship.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        # Start each new ship at the bottom center of the screen.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        # Store a decimal value for the ship's center. w
        self.center = float(self.rect.centerx)

        # Movement flags
        self.moving_right = False
        self.moving_left = False



    def update(self):
        """Update the ship's position based on the movement flags."""
        # Update the ship's center value, not the rect.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.player_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.player_speed_factor
        # Update rect object from self.center. y
        self.rect.centerx = self.center

        #Define initial stats
        self.health = 100
        self.attack = 10
        self.armour = 5
        self.magicDamage = 15
        self.exp = 0
        self.expr = 100
        self.level = 1
    def blitme(self):
        """Draw the player at its current location."""
        self.screen.blit(self.image, self.rect)
