import pygame
from constants import *
from player import Player

def __main__():
    print("Starting Asteroids!"
    f"\nScreen width: {SCREEN_WIDTH}"
    f"\nScreen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        dt = clock.tick(60)/1000
        player.draw(screen)
        player.update(dt)
        pygame.display.flip()
    
if __name__ == "__main__":
    __main__()