import pygame
from constants import *
from player import Player
from asteroidfield import AsteroidField
from asteroid import Asteroid
from shot import Shot


def main():
    pygame.init()
    main_surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    fps = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Shot.containers = (updatable, drawable)

    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)

    AsteroidField.containers = (updatable, )
    asteroid_field = AsteroidField()

    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    while (True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        main_surface.fill((0, 0, 0))

        for object in drawable:
            object.draw(main_surface)

        for object in updatable:
            object.update(dt)

        for asteroid in asteroids:
            if asteroid.collide(player):
                print("Game Over!")
                return

            for shot in drawable:
                if type(shot) is Shot:
                    if shot.collide(asteroid):
                        asteroid.split()
                        shot.kill()

        pygame.display.flip()
        dt = (fps.tick(60))/1000


if __name__ == "__main__":
    main()
