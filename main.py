import pygame
from constants import *
from player import Player


def main():
    # basic pygame setup
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    color = 0,0,0
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    # pygame clock object to keep track of time elapsed - dt is delta time (aka time passed since last update)
    clock = pygame.time.Clock()
    dt = 0

    # creating player object(s)
    

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill(color)
        player.draw(screen)
        player.update(dt)
        pygame.display.flip()


        # limit the framerate to 60fps
        dt = clock.tick(60) / 1000

        
        



if __name__ == "__main__":
    main()
