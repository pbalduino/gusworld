#!/usr/bin/env python3
import sys, pygame
import pygame.freetype as freetype


def initialize():
    print("Initializing")
    pygame.display.init()

    freetype.init()
    font = freetype.Font("pincoyablack.otf")

    print(font)

    light_blue = [135, 206, 235]
    size = width, height = 640, 480
    screen = pygame.display.set_mode(size)
    # pygame.draw.rect(screen, light_blue, pygame.Rect(0, 0, 640, 480))
    screen.fill(light_blue)
    font.render_to(screen, (64, 32), "Gustavo World", fgcolor = pygame.Color(220, 30, 30), size = 64)
    pygame.display.flip()

def read_input():
    pygame.event.pump()
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT]:
        print("Left")
    if key[pygame.K_RIGHT]:
        print("Right")


def handle_exit():
    for event in pygame.event.get():
        pygame.display.flip()
        if event.type == pygame.QUIT:
            print("Bye!")
            pygame.quit()
            sys.exit()


def game_loop():
    print("Starting game loop")
    while 1:
        read_input()
        handle_exit()
        pygame.time.delay(20)

initialize()
game_loop()
