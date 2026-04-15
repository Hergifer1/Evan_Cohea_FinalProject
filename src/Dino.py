import pygame
import random

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        
        #Running
        self.running_frames = [
            pygame.image.load('Dino_Running1').convert_alpha(),
            pygame.image.load('Dino_Running2').convert_alpha()
        ]
        self.running_frames = [pygame.transform.scale(frame, (100, 100)) for frame in self.running_frames]
        
        #Ducking
        duck_frames = [
            pygame.image.load('Dino_Ducking1.png').convert_alpha(),
            pygame.image.load('Dino_Ducking2.png').convert_alpha()
        ]
        for sprite in duck_frames:
            sprite = pygame.transform.scale(sprite, (100, 100))
        
        #Standing
        Dino = pygame.image.load('Dino_Standing.png')
        Dino = pygame.transform.scale(Dino, (100, 100))
        Dino_rect = Dino.get_rect()
        Dino_rect.bottomleft = (0, 400)
        
def main():
    pygame.init()
    pygame.display.set_caption("Dinosaur Game")
    screen = pygame.display.set_mode((800, 500))
    clock = pygame.time.Clock()
    running = True
    frame = 0
    animation_speed = 0.5
    x, y = 0, 400
    player = Player(x, y)
    
    #Dino = pygame.image.load('Dino_Standing.png')
    #Dino = pygame.transform.scale(Dino, (100, 100))
    
    #Dino_rect = Dino.get_rect()
    #Dino_rect.bottomleft = (0, 400)
    while running:
        screen.fill((0, 0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        frame += animation_speed
        if frame >= len(player.running_frames):
            frame = 0

        current_frame = player.running_frames[int(frame)]
        screen.blit(current_frame, (x, y))
        
        pygame.display.flip()
        clock.tick(60)
if __name__ == "__main__":
    main()