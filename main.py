import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
def main():

    print("Starting asteroids!")
    print("Screen width:",SCREEN_WIDTH)
    print("Screen height:",SCREEN_HEIGHT)

    pygame.init()
    running = True
    clock=pygame.time.Clock()
    dt=0

    if(pygame.get_init()):
        screen=pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))


        updatable=pygame.sprite.Group()
        drawable=pygame.sprite.Group()
        asteroids=pygame.sprite.Group()
        AsteroidField.containers=(updatable)
        Asteroid.containers=(asteroids,updatable,drawable)
        Player.containers=(updatable,drawable)
        
        player=Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
        asteroidField=AsteroidField()
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            screen.fill("black")

            for i in updatable:
                i.update(dt)
            for j in drawable:
                j.draw(screen)
            for asteroid in asteroids:
                if asteroid.checkCollision(player):
                    exit()
            pygame.display.flip()

            fps=clock.tick(60)
            dt=fps/1000

if __name__=="__main__":
    main()
