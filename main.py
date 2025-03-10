import pygame
from constants import *
from player import Player


def main():
    pygame.init()
    main_surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    fps = pygame.time.Clock()
    dt = 0
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    while (True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        main_surface.fill((0, 0, 0))
        player.draw(main_surface)

        pygame.display.flip()
        dt = (fps.tick(60))/1000


if __name__ == "__main__":
    main()
