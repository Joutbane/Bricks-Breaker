#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
from pygame import Surface, Rect
from pygame.font import Font

from code.const import WIN_WIDTH, COLOR_WHITE, MENU_OPTION, COLOR_GREY


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./assets/MenuBg.png')
        self.rect = self.surf.get_rect()

    def run(self, ):
        pygame.mixer_music.load('./assets/SoundMenu.wav')
        pygame.mixer_music.play(-1)
        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text(100,"BRICKS BREAKER", (COLOR_GREY), (WIN_WIDTH / 2, 200))


            for i in range(len(MENU_OPTION)):
                self.menu_text(75, MENU_OPTION[i], (COLOR_WHITE), (WIN_WIDTH / 2, 400 + 100 * i))

            pygame.display.flip()

            # Check for all events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()  # Close screen
                    quit()  # end pygame


    def menu_text(self, text_size:int, text: str, text_color: tuple, text_center_pos: tuple  ):
        text_font: Font = pygame.font.SysFont(name='Orbitron', size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)
