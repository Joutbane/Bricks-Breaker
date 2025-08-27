import sys

import pygame

pygame.init()
screen = pygame.display.set_mode((750, 900))

while True:
    # Check for all events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() # Close screen
            quit() # end pygame
