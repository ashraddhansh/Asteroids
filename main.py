import pygame
from pygame.display import update
from asteroids import *
from constants import *
from asteroidfield import *
from player import *
import sys
from shot import *

from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = (asteroids,updatable,drawable)
    Shot.containers = (shots,updatable,drawable)
    AsteroidField.containers = updatable
    asterofield = AsteroidField()

    Player.containers = (updatable, drawable)

    player = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)

    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        updatable.update(dt)
        for asteroid in asteroids:
            if asteroid.checkcollisions(player):
                print("Game Over!")
                sys.exit()

            for shot in shots:
                if asteroid.checkcollisions(shot):
                    asteroid.kill()
                    shot.kill()


        screen.fill("black")

        for obj in drawable:
            obj.draw(screen)


        pygame.display.flip()
        dt = clock.tick(60)/1000

if __name__ == "__main__":
    main()
