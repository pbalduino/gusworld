#!/usr/bin/env python3
import sys
import pygame
import pygame.freetype as freetype

sgus = None

def start_screen():
    print("loading color")
    red = pygame.Color(220, 30, 30)
    transparent = pygame.Color(249, 43, 237)
    print("loading font")
    title_font = freetype.Font("data/pincoyablack.otf", 64)
    small_font = freetype.Font("data/YanoneKaffeesatz-Regular.ttf", 32)

    print("font ok")
    light_blue = [135, 206, 235]

    size = width, height = 640, 480
    title = "Gustavo World"
    subtitle = "A game about discovery and learning"
    _, _, t_width, t_height = title_font.get_rect(title)
    t_center = int((640 - t_width) / 2)

    _, _, st_width, _ = small_font.get_rect(subtitle)
    st_center = int((640 - st_width) / 2)
    print("center ok")

    print(t_width)
    print(t_center)

    screen = pygame.display.set_mode(size)

    screen.fill(light_blue)
    title_font.render_to(screen, (t_center, 48), title, red)
    small_font.render_to(screen, (st_center, 48 + t_height + 5), subtitle, red)

    gus = pygame.image.load("data/gus_1.png").convert()
    gus.set_colorkey(transparent)
    sgus = pygame.transform.scale(gus, (int(gus.get_width() * 0.4), int(gus.get_height() * 0.4)))
    screen.blit(sgus, (10, 310))

def initialize():
    print("Initializing")
    pygame.display.init()

    freetype.init()
    start_screen()
    pygame.display.flip()


def read_input():
    pygame.event.pump()
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT]:
        print("Left")
        print(sgus.get_width())
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
