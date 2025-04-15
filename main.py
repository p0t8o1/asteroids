import pygame
from constants import *

def __main__():
    print("Starting Asteroids!"
    f"\nScreen width: {SCREEN_WIDTH}"
    f"\nScreen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        pygame.display.flip()
    
if __name__ == "__main__":
    __main__()