import pygame
from constants import *
from player import *

def main():
    if not pygame.get_init():
        pygame.init()
    
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    clock = pygame.time.Clock()
    dt = 0

    player_avatar = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        player_avatar.draw(screen)
        screen.fill(pygame.Color(0, 0, 0))
        pygame.display.flip()

        dt = clock.tick(60) / 1000
    
if __name__== "__main__":
    main()