import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot


def main():
    # basic pygame setup
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    color = 0,0,0

    # creating groups
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    
    Player.containers = (updateable, drawable)
    Asteroid.containers = (asteroids, updateable, drawable)
    Shot.containers = (shots, updateable, drawable)
    AsteroidField.containers = (updateable)

    asteroid_field = AsteroidField()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    # pygame clock object to keep track of time elapsed - dt is delta time (aka time passed since last update)
    clock = pygame.time.Clock()
    dt = 0

  

    updateable.add(player)
    drawable.add(player)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        for obj in updateable:
            obj.update(dt)

        for asteroid in asteroids:
            if asteroid.collides_with(player):
                print("Game over!")
                sys.exit()

        for asteroid in asteroids:
            for bullet in shots:
                if asteroid.collides_with(bullet):
                    asteroid.kill()
                    bullet.kill()
                
        screen.fill(color)
        
        for obj in drawable:
            obj.draw(screen)
 
        pygame.display.flip()
        # limit the framerate to 60fps
        dt = clock.tick(60) / 1000

        
        



if __name__ == "__main__":
    main()
