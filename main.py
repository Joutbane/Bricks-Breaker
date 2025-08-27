import sys

import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))

while True:
    # Check for all events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() # Clos screen
            quit() # end pygame
