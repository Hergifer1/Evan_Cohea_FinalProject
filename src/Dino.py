import pygame
import random


def main():
    pygame.init()
    pygame.display.set_caption("Dinosaur Game")
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((500, 600))
    running = True
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.flip()