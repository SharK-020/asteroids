import pygame
from constants import *
from player import Player
def main():

    pygame.init()
    running = True
    clock=pygame.time.Clock()
    dt=0

    if(pygame.get_init()):
        screen=pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
        player=Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            screen.fill("black")
            player.update(dt)
            player.draw(screen)
            pygame.display.flip()

            fps=clock.tick(60)
            dt=fps/1000

    print("Starting asteroids!")
    print("Screen width:",SCREEN_WIDTH)
    print("Screen height:",SCREEN_HEIGHT) 


if __name__=="__main__":
    main()
