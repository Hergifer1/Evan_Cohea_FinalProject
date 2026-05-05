import pygame
import random
import math
pygame.mixer.init()

pygame.font.init()
gamefont = pygame.font.SysFont("Lucida Console", 32)
gamefont2 = pygame.font.SysFont("Lucida Console", 16)
gamestart = gamefont.render("Press Space to Start", True, (125, 125, 125))
gameover = gamefont.render("Game Over", True, (125, 125, 125))
retry = gamefont2.render("Press 'r' to try again or 'q' to quit", True, (125, 125, 125))
scores = []
width = 800
height = 500
jump_sound = pygame.mixer.Sound('Dino_jumpsound.mp3')
hurt_sound = pygame.mixer.Sound('Dino_hurtsound.mp3')
coin_sound = pygame.mixer.Sound('Dino_coinsound.mp3')

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

        #variables
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

    def player_rect(self):
        if self.is_ducking:    
            return pygame.Rect(self.x + 10, self.y + 50, 80, 60)
        elif self.is_jumping:
            return pygame.Rect(self.x + 20, self.y + 10, 65, 65)
        else:
            return pygame.Rect(self.x + 20, self.y + 25, 65, 65)

    def jump(self):
        if not self.is_jumping:
            jump_sound.play()
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

    def draw(self, screen, over=False):
        if self.is_jumping:
            screen.blit(self.Dino_stand, (self.x, self.y))
        
        elif self.is_ducking:
            current_frame = self.ducking_frames[int(self.frame)]
            screen.blit(current_frame, (self.x, self.y))

            if not over:
                self.frame += self.animation_speed
                if self.frame >= len(self.ducking_frames):
                    self.frame = 0
        
        else:
            current_frame = self.running_frames[int(self.frame)]
            screen.blit(current_frame, (self.x, self.y))

            if not over:
                self.frame += self.animation_speed
                if self.frame >= len(self.running_frames):
                    self.frame = 0

class Obstacle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        #Cacti
        self.cacti1 = pygame.image.load('Cactus_1.png').convert_alpha()
        self.cacti1 = pygame.transform.scale(self.cacti1, (80, 80))

        self.cacti2 = pygame.image.load('Cactus_2.png').convert_alpha()
        self.cacti2 = pygame.transform.scale(self.cacti2, (80, 80))

        self.cactiDuo = pygame.image.load('Cactus_Duo.png').convert_alpha()
        self.cactiDuo = pygame.transform.scale(self.cactiDuo, (80, 80))

        self.cactiTrio = pygame.image.load('Cactus_Trio.png').convert_alpha()
        self.cactiTrio = pygame.transform.scale(self.cactiTrio, (80, 80))

        self.cacti = [self.cacti1, self.cacti2, self.cactiDuo, self.cactiTrio]

        self.cact = random.choice(self.cacti)

        #Pterodactyl
        self.Pterodactyl = [
            pygame.image.load('Ptero_1.png').convert_alpha(),
            pygame.image.load('Ptero_2.png').convert_alpha()
        ]
        self.Pterodactyl = [pygame.transform.scale(frame, (100, 100)) for frame in self.Pterodactyl]

        self.ptero_chance = random.randint(1, 5)

        #variables
        self.frame = 0
        self.animation_speed = 0.05
        self.x = 800
        self.y =  345
        self.ptero_height = random.randint(200, 340)
 
    def obstacle_rect(self):
        if self.ptero_chance == 3:
            return pygame.Rect(self.x + 20, self.ptero_height + 20, 70, 60)
        else:
            return pygame.Rect(self.x + 5, self.y + 10, 70, 70)

    def update(self, speed):
        self.x -= speed
  
    def draw(self, screen, over=False):
        if self.ptero_chance == 3:
            current_frame = self.Pterodactyl[int(self.frame)]
            screen.blit(current_frame, (self.x, self.ptero_height))

            if not over:
                self.frame += self.animation_speed
                if self.frame >= len(self.Pterodactyl):
                    self.frame = 0

        else:
            screen.blit(self.cact, (self.x, self.y))

    def is_off_screen(self):
        return self.x < -100

class Coins(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        #coin
        self.coin = pygame.image.load('Dino_coin.png').convert_alpha()
        self.coin = pygame.transform.scale(self.coin, (70, 70))
        self.x = 800
        self.coin_height = random.randint(200, 340)

    def coin_rect(self):
        return pygame.Rect(self.x + 20, self.coin_height + 20, 30, 30)
        
    def update(self, speed):
        self.x -= speed

    def draw(self, screen, over=False):
        screen.blit(self.coin, (self.x, self.coin_height))

    def is_off_screen(self):
        return self.x < -100
        
def main():
    pygame.init()
    pygame.display.set_caption("Dinosaur Game")
    screen = pygame.display.set_mode((width, height))
    clock = pygame.time.Clock()
    running = False
    start = True
    over = False
    rewind_time = pygame.time.get_ticks()
    obstacles = []
    coins = []
    
    lastobs_spawn = 0
    lastcoin_spawn = 0
    obsspawn_delay = random.randint(1500, 3000)
    coinspawn_delay = random.randint(4000, 8000)
    
    game_speed = 9

    #ground
    ground = pygame.image.load('Dino_Ground.png').convert_alpha()
    scroll = 0
    i = 0
    tiles = math.ceil(width / ground.get_width()) + 1

    player = Player()
    
    Dino_start = pygame.image.load('Dino_Standing.png').convert_alpha()
    Dino_start = pygame.transform.scale(Dino_start, (100, 100))
    
    while start:
        screen.fill((225, 225, 225))
        screen.blit(gamestart, (200, 250))
        screen.blit(Dino_start, (27, 340))
        screen.blit(ground, (ground.get_width()*i + scroll, 410))

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    running = True
                    start = False

        pygame.display.flip()
    while running:
        screen.fill((225, 225, 225))

        if not over:
            #display clock
            time = (pygame.time.get_ticks() - rewind_time) // 100
            timer = gamefont.render(f'{time}', True, (125, 125, 125))

            #Sets obstacle spawn rate
            current_time = pygame.time.get_ticks()
            if current_time - lastobs_spawn > obsspawn_delay:
                obstacles.append(Obstacle())
                lastobs_spawn = current_time

                #Sets random delay for the next spawn
                obsspawn_delay = random.randint(520, 1500)

            #Set coin spawn rate
            coin_time = pygame.time.get_ticks()
            if coin_time - lastcoin_spawn > coinspawn_delay:
                coins.append(Coins())
                lastcoin_spawn = current_time

                #Sets random delay for the next spawn
                coinspawn_delay = random.randint(4000, 8000)

            #Increments speed of the game
            game_speed += 0.002
            if game_speed > 20:
                game_speed = 20

            #Updates obstacles
            for obstacle in obstacles[:]:
                obstacle.update(game_speed)
                obstacle.draw(screen, over)

                if obstacle.is_off_screen():
                    obstacles.remove(obstacle)

            #Updates coins
            for coin in coins[:]:
                coin.update(game_speed)
                coin.draw(screen, over)

                if coin.is_off_screen():
                    coins.remove(coin)
            
            #ground scrolling        
            scroll -= game_speed
            if abs(scroll) > ground.get_width():
                scroll = 0

            player.update()
            #Check collision
            player_rect = player.player_rect()
            for obstacle in obstacles:
                if player_rect.colliderect(obstacle.obstacle_rect()):
                    over = True
                    hurt_sound.play()

            for coin in coins:
                if player_rect.colliderect(coin.coin_rect()):
                    coin_sound.play()
                    coins.remove(coin)
                    rewind_time -= 10000

                for obstacle in obstacles:
                    if coin.coin_rect().colliderect(obstacle.obstacle_rect()):
                        coins.remove(coin)

        #Checking for events
        for event in pygame.event.get():
            
        #Quitting
            if event.type == pygame.QUIT:
                running = False
            if over:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        main()
                        return
                    if event.key == pygame.K_q:
                        running = False

        #Character controls
            if not over:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        
                        player.jump()

                    if event.key == pygame.K_DOWN:
                        player.duck()
                    
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_DOWN:
                        player.notduck()
        
        #Draws obstacles after game over
        i = 0
        while (i < tiles):
            screen.blit(ground, (ground.get_width()*i + scroll, 410))
            i += 1
        
        for obstacle in obstacles:
            obstacle.draw(screen, over)
        
        for coin in coins:
            coin.draw(screen, over)
        
        player.draw(screen, over)   
        
        timer_rect = timer.get_rect(topright=(780, 20))
        screen.blit(timer, timer_rect)
        
        if over:
            screen.blit(gameover, (300, 250))
            screen.blit(retry, (200, 280))
            scores.append(time)
            high_score = gamefont2.render(f"High Score: {max(scores)}", True, (125, 125, 125))
            screen.blit(high_score, (310, 300))
        
        #Animate Dino              
        pygame.display.flip()
        clock.tick(60)
if __name__ == "__main__":
    main()