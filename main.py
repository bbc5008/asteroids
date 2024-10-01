import pygame
from constants import *
from player import Player

def main():
    if not pygame.get_init():
        pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    player_avatar = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    dt = 0

    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        #update stuff
        player_avatar.update(dt)    

        #draw stuff
        screen.fill('black')
        player_avatar.draw(screen)
        pygame.display.flip()

        dt = clock.tick(60) / 1000
    
if __name__== "__main__":
    main()