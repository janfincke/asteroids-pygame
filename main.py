import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_WIDTH))
    while True:
        screen.fill("black")

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return


        pygame.display.flip()
if __name__ == "__main__":
    main()
