import random
import sys

import pygame

from src.utils.file import FileManager


class FlappyBird:
    def __init__(self):
        pygame.mixer.pre_init(frequency=44100, size=-16, channels=2, buffer=512)
        pygame.init()
        pygame.display.set_caption('Flappy Bird Game')
        self.screen = pygame.display.set_mode((800, 600))
        self.clock = pygame.time.Clock()
        self.game_font = pygame.font.SysFont('Roboto', 35)

        # Create variable
        self.gravity = 0.25
        self.bird_movement = 0
        self.game_active = False
        self.score = 0
        self.high_score = 0
        self.lose = False

        # Create background
        self.bg = FileManager().load_image('image/flappy-bird/background-night.png', True)
        self.bg = pygame.transform.scale(self.bg, (800, 600))
        
        # Create floor
        self.floor = FileManager().load_image('image/flappy-bird/floor.png', True)
        self.floor_x_pos = 0
        
        # Create bird
        self.bird_down = FileManager().load_image('image/flappy-bird/yellowbird-downflap.png', True)
        self.bird_mid = FileManager().load_image('image/flappy-bird/yellowbird-midflap.png', True)
        self.bird_up = FileManager().load_image('image/flappy-bird/yellowbird-upflap.png', True)
        self.bird_list = [self.bird_down, self.bird_mid, self.bird_up]  #0 1 2
        self.bird_index = 0
        self.bird = self.bird_list[self.bird_index]
        self.bird_rect = self.bird.get_rect(center=(80, 300))

        # Create timer
        self.bird_flap = pygame.USEREVENT + 1
        pygame.time.set_timer(self.bird_flap, 200)
        
        # Create Pipe
        self.pipe_surface = FileManager().load_image('image/flappy-bird/pipe-green.png', True)
        self.pipe_list = []
        
        # Create timer
        self.spawn_pipe = pygame.USEREVENT
        pygame.time.set_timer(self.spawn_pipe, 1000)
        self.pipe_height = [300, 350, 400]

        # Game over
        self.game_over_surface = pygame.transform.scale2x(FileManager().load_image('image/flappy-bird/message.png', True))
        self.game_over_rect = self.game_over_surface.get_rect(center=(400, 250))
        # Add sound
        self.flap_sound = pygame.mixer.Sound(FileManager().resource_path('sound/flappy-bird/sfx_wing.wav'))
        self.hit_sound = pygame.mixer.Sound(FileManager().resource_path('sound/flappy-bird/sfx_hit.wav'))
        self.score_sound = pygame.mixer.Sound(FileManager().resource_path('sound/flappy-bird/sfx_point.wav'))
        self.score_sound_countdown = 100

    def draw_floor(self):
        self.screen.blit(self.floor, (self.floor_x_pos, 500))
        self.screen.blit(self.floor, (self.floor_x_pos + 800, 500))

    def create_pipe(self):
        self.random_pipe_pos = random.choice(self.pipe_height)
        self.top_pipe = self.pipe_surface.get_rect(midtop=(800, self.random_pipe_pos - 450))
        self.bottom_pipe = self.pipe_surface.get_rect(midtop=(800, self.random_pipe_pos))

        return self.bottom_pipe, self.top_pipe

    def move_pipe(self, pipes):
        for pipe in pipes:
            pipe.centerx -= 5
        return pipes

    def draw_pipe(self, pipes):
        for pipe in pipes:
            if pipe.bottom >= 600:
                self.screen.blit(self.pipe_surface, pipe)
            else:
                flip_pipe = pygame.transform.flip(self.pipe_surface, False, True)
                self.screen.blit(flip_pipe, pipe)

    def check_collision(self, pipes):
        for pipe in pipes:
            if self.bird_rect.colliderect(pipe):
                self.hit_sound.play()
                self.lose = True
                return False
        if self.bird_rect.top <= -50 or self.bird_rect.bottom >= 520:
            self.lose = True
            return False
        return True

    def rotate_bird(self, bird1):
        new_bird = pygame.transform.rotozoom(bird1, -self.bird_movement * 1, 1)
        return new_bird

    def bird_animation(self):
        new_bird = self.bird_list[self.bird_index]
        new_bird_rect = new_bird.get_rect(center=(100, self.bird_rect.centery))
        return new_bird, new_bird_rect

    def score_display(self, game_state):
        if game_state == 'main game_temp':
            score_surface = self.game_font.render(str(int(self.score)), True, (255, 255, 255))
            score_rect = score_surface.get_rect(center=(216, 100))
            self.screen.blit(score_surface, score_rect)
        if game_state == 'game_over':
            score_surface = self.game_font.render(f'Score: {int(self.score)}', True, (255, 255, 255))
            score_rect = score_surface.get_rect(center=(216, 100))
            self.screen.blit(score_surface, score_rect)

            high_score_surface = self.game_font.render(f'High Score: {int(self.high_score)}', True, (255, 255, 255))
            high_score_rect = high_score_surface.get_rect(center=(216, 630))
            self.screen.blit(high_score_surface, high_score_rect)

    def update_score(self, score, high_score):
        if score > high_score:
            high_score = score
        return high_score

    def run(self):
        while True:
            self.screen.blit(self.bg, (0, 0))
            if len(self.pipe_list) > 0:
                if self.pipe_list[0].x < 0:
                    self.score_sound.play()
                    self.score += 1
                    self.pipe_list.pop(0)
                    self.pipe_list.pop(0)
            # if game_active is False:
            #     screen.blit(bird,bird_rect)

            if self.game_active:
                #chim
                self.bird_movement += self.gravity
                rotated_bird = self.rotate_bird(self.bird)
                self.bird_rect.centery += self.bird_movement
                self.screen.blit(rotated_bird, self.bird_rect)
                self.game_active = self.check_collision(self.pipe_list)
                #ống
                self.pipe_list = self.move_pipe(self.pipe_list)
                self.draw_pipe(self.pipe_list)
                # score += 0.01
                self.score_display('main game_temp')
                # score_sound_countdown -= 1
                # if score_sound_countdown <= 0:
                #     score_sound.play()
                #     score_sound_countdown = 100
            else:
                self.screen.blit(self.game_over_surface, self.game_over_rect)
                self.high_score = self.update_score(self.score, self.high_score)
                # if lose is True:
                #     score_display('game_over')
                self.screen.blit(self.bird, self.bird_rect)
            #sàn
            self.floor_x_pos -= 1
            self.draw_floor()
            if self.floor_x_pos <= -800:
                self.floor_x_pos = 0

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE and self.game_active:
                        self.bird_movement = -4
                        self.flap_sound.play()
                    if event.key == pygame.K_SPACE and self.game_active == False:
                        self.game_active = True
                        self.pipe_list.clear()
                        self.bird_rect.center = (100, 300)
                        self.bird_movement = 0
                        self.score = 0
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1 and self.game_active:
                        self.bird_movement = -4
                        self.flap_sound.play()
                    if event.button == 1 and self.game_active == False:
                        self.game_active = True
                        self.pipe_list.clear()
                        self.bird_rect.center = (100, 300)
                        self.bird_movement = 0
                        self.score = 0
                if event.type == self.spawn_pipe:
                    self.pipe_list.extend(self.create_pipe())

                    # print( "x= ",pipe_list[0].x)
                    # print( "right= ",pipe_list[0].right)
                    # print( "bird_rect.left= ",bird_rect.left)
                    # print( "bird_rect.x= ",bird_rect.x)
                    # print(pipe_list)
                    # if pipe_list[0].x < bird_rect.right :
                if event.type == self.bird_flap:
                    if self.bird_index < 2:
                        self.bird_index += 1
                    else:
                        self.bird_index = 0
                    self.bird, self.bird_rect = self.bird_animation()

            pygame.display.update()
            self.clock.tick(60)
