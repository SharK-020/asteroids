import pygame
from constants import *

def main():

    pygame.init()
    running = True
    if(pygame.get_init()):
        screen=pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            screen.fill("black")
            pygame.display.flip()

    print("Starting asteroids!")
    print("Screen width:",SCREEN_WIDTH)
    print("Screen height:",SCREEN_HEIGHT) 


if __name__=="__main__":
    main()
