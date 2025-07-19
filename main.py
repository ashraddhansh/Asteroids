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
    dt = 0
    clock = pygame.time.Clock()
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids,updatable,drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots,updatable,drawable)

    asterofield = AsteroidField()



    player = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
    updatable.add(player)
    drawable.add(player)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        updatable.update(dt)
        for asteroid in asteroids:
            if asteroid.checkcollisions(player):
                print("Game Over!")
                sys.exit()


        screen.fill("black")

        for obj in drawable:
            obj.draw(screen)


        pygame.display.flip()
        dt = clock.tick(60)/1000

if __name__ == "__main__":
    main()
