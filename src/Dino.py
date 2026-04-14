import pygame
import random

def main():
    pygame.init()
    pygame.display.set_caption("Dinosaur Game")
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((800, 500))
    running = True

    #Create character
    Dino = pygame.image.load('Dino_Standing.png')
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((0, 0, 0))
        
        pygame.display.flip()

if __name__ == "__main__":
    main()