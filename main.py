import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    if not pygame.get_init():
        pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updateable_group = pygame.sprite.Group()
    drawable_group = pygame.sprite.Group()
    asteroids_group = pygame.sprite.Group()
    shot_group = pygame.sprite.Group()

    Player.containers = (updateable_group, drawable_group)
    Asteroid.containers = (asteroids_group, updateable_group, drawable_group)
    AsteroidField.containers = (updateable_group)
    Shot.containers = (shot_group, updateable_group, drawable_group)


    
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()
    dt = 0

    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        #update stuff
        #player_avatar.update(dt)
        for object in updateable_group:
            object.update(dt)

            

        for asteroid in asteroids_group:
            if asteroid.collision_check(player):
                print("GAME OVER!")
                sys.exit()

            for shot in shot_group:
                if asteroid.collision_check(shot): 
                    shot.kill()
                    asteroid.split()
            
        

        #draw stuff
        screen.fill('black')
        #player_avatar.draw(screen)
        for object in drawable_group:
            object.draw(screen)
        pygame.display.flip()

        dt = clock.tick(60) / 1000
    
if __name__== "__main__":
    main()