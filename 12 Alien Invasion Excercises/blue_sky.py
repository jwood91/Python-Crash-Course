import sys
import pygame
from arnold import Arnold


def run_game():
    """Initilise game and make blue window"""
    pygame.init()

    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Blue Sky")

    bg_colour = (0, 0, 255)
    arnold = Arnold(screen)

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        screen.fill(bg_colour)
        arnold.blitme()

        pygame.display.flip()


run_game()
