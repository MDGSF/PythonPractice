#! /usr/bin/env python

import pygame
from pygame.locals import *
from sys import exit

SCREEN_SIZE = (640, 480)
background_image_filename = "../resource/sushiplate.jpg"


def main():
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE, 0, 32)
    background = pygame.image.load(background_image_filename).convert()

    fullScreen = False

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
            if event.type == KEYDOWN:
                if event.key == K_f:
                    fullScreen = not fullScreen
                    if fullScreen:
                        screen = pygame.display.set_mode((640, 480), FULLSCREEN, 32)
                    else:
                        screen = pygame.display.set_mode(SCREEN_SIZE, 0, 32)

        screen.blit(background, (0, 0))
        pygame.display.update()


if __name__ == '__main__':
    main()
