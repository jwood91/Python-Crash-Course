import pygame


class Arnold():

    def __init__(self, screen):
        """Initilise the arnold class"""
        self.screen = screen

        # Load Arnold image and get its rect
        self.image = pygame.image.load('arnold.bmp')
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Start each new arnold center bottom
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        """Draw Arnold at its current location"""
        self.screen.blit(self.image, self.rect)
