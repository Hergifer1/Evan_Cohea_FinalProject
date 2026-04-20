import pygame
import random

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        
        #Running
        self.running_frames = [
            pygame.image.load('Dino_Running1.png').convert_alpha(),
            pygame.image.load('Dino_Running2.png').convert_alpha()
        ]
        self.running_frames = [pygame.transform.scale(frame, (100, 100)) for frame in self.running_frames]
        
        #Ducking
        self.ducking_frames = [
            pygame.image.load('Dino_Ducking1.png').convert_alpha(),
            pygame.image.load('Dino_Ducking2.png').convert_alpha()
        ]
        self.ducking_frames = [pygame.transform.scale(frame, (100, 100)) for frame in self.ducking_frames]
        
        #Standing
        self.Dino_stand = pygame.image.load('Dino_Standing.png').convert_alpha()
        self.Dino_stand = pygame.transform.scale(self.Dino_stand, (100, 100))

        self.frame = 0
        self.animation_speed = 0.2
        
        self.x = 30
        self.y = 325
        self.ground_y = self.y
        
        self.velocity_y = 0
        self.gravity = 1
        self.jump_strength = -18
        self.is_jumping = False
        self.is_ducking = False

    def jump(self):
        if not self.is_jumping:
            self.velocity_y = self.jump_strength
            self.is_jumping = True
    
    def update(self):
        if self.is_jumping:
            self.velocity_y += self.gravity
            self.y += self.velocity_y

            if self.y >= self.ground_y:
                self.y = self.ground_y
                self.velocity_y = 0
                self.is_jumping = False

    def duck(self):
            if not self.is_jumping and not self.is_ducking:
                self.is_ducking = True

    def notduck(self):
        if self.is_ducking:
            self.is_ducking = False

    def draw(self, screen):
        if self.is_jumping:
            screen.blit(self.Dino_stand, (self.x, self.y))
        
        elif self.is_ducking:
            current_frame = self.ducking_frames[int(self.frame)]
            screen.blit(current_frame, (self.x, self.y))

            self.frame += self.animation_speed
            if self.frame >= len(self.ducking_frames):
                self.frame = 0
        
        else:
            current_frame = self.running_frames[int(self.frame)]
            screen.blit(current_frame, (self.x, self.y))

            self.frame += self.animation_speed
            if self.frame >= len(self.running_frames):
                self.frame = 0

def main():
    pygame.init()
    pygame.display.set_caption("Dinosaur Game")
    screen = pygame.display.set_mode((800, 500))
    clock = pygame.time.Clock()
    running = True

    player = Player()
    

    while running:
        screen.fill((0, 0, 0))

        for event in pygame.event.get():
            
        #Quitting
            if event.type == pygame.QUIT:
                running = False

        #Jummping
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    player.jump()

                if event.key == pygame.K_DOWN:
                    player.duck()
                    
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_DOWN:
                    player.notduck()
        
        player.update()
        player.draw(screen)

        #Animate Dino       
        pygame.display.flip()
        clock.tick(60)
if __name__ == "__main__":
    main()