import random

import pygame


class FlappyBird:
    def __init__(self):
        pygame.mixer.pre_init(frequency=44100, size=-16, channels=2, buffer=512)
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        self.clock = pygame.time.Clock()
        self.game_font = pygame.font.Font('04B_19.ttf', 35)
        # Create variable
        self.gravity = 0.25
        self.bird_movement = 0
        self.game_active = False
        self.score = 0
        self.high_score = 0
        self.lose = False
        # Create background
        self.bg = pygame.image.load('assets/background-night.png').convert()
        self.bg = pygame.transform.scale(bg, (800, 600))
        # Create floor
        self.floor = pygame.image.load('assets/floor.png').convert()
        # floor = pygame.transform.scale2x(floor)
        self.floor_x_pos = 0
        # Create bird
        self.bird_down = pygame.image.load('assets/yellowbird-downflap.png').convert_alpha()
        self.bird_mid = pygame.image.load('assets/yellowbird-midflap.png').convert_alpha()
        self.bird_up = pygame.image.load('assets/yellowbird-upflap.png').convert_alpha()
        self.bird_list = [self.bird_down, self.bird_mid, self.bird_up]  #0 1 2
        self.bird_index = 0
        self.bird = self.bird_list[self.bird_index]
        #bird= pygame.image.load('assets/yellowbird-midflap.png').convert_alpha()
        #bird = pygame.transform.scale2x(bird)
        self.bird_rect = self.bird.get_rect(center=(80, 300))

        # Create timer
        self.birdflap = pygame.USEREVENT + 1
        pygame.time.set_timer(self.birdflap, 200)
        # Create Pipe
        self.pipe_surface = pygame.image.load('assets/pipe-green.png').convert()
        # pipe_surface = pygame.transform.scale2x(pipe_surface)
        self.pipe_list = []
        # Create timer
        self.spawnpipe = pygame.USEREVENT
        pygame.time.set_timer(self.spawnpipe, 1000)
        self.pipe_height = [300, 350, 400]
        # Game over
        self.game_over_surface = pygame.transform.scale2x(pygame.image.load('assets/message.png').convert_alpha())
        self.game_over_rect = self.game_over_surface.get_rect(center=(400, 250))
        # Add sound
        self.flap_sound = pygame.mixer.Sound('sound/sfx_wing.wav')
        self.hit_sound = pygame.mixer.Sound('sound/sfx_hit.wav')
        self.score_sound = pygame.mixer.Sound('sound/sfx_point.wav')
        self.score_sound_countdown = 100

    def draw_floor(self):
        self.screen.blit(self.floor, (self.floor_x_pos, 500))
        self.screen.blit(self.floor, (self.floor_x_pos + 800, 500))


    def create_pipe(self):
        self.random_pipe_pos = random.choice(self.pipe_height)
        self.top_pipe = self.pipe_surface.get_rect(midtop=(800, random_pipe_pos - 450))
        self.bottom_pipe = self.pipe_surface.get_rect(midtop=(800, random_pipe_pos))

        return self.bottom_pipe, self.top_pipe


    def move_pipe(pipes):
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


    def rotate_bird(bird1):
        new_bird = pygame.transform.rotozoom(bird1, -bird_movement * 1, 1)
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


    def update_score(score, high_score):
        if score > high_score:
            high_score = score
        return high_score

    def run(self):
        while True:
            self.screen.blit(bg, (0, 0))
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
                bird_movement += gravity
                rotated_bird = rotate_bird(bird)
                bird_rect.centery += bird_movement
                screen.blit(rotated_bird, bird_rect)
                game_active = check_collision(pipe_list)
                #ống
                pipe_list = move_pipe(pipe_list)
                draw_pipe(pipe_list)
                # score += 0.01
                score_display('main game_temp')
                # score_sound_countdown -= 1
                # if score_sound_countdown <= 0:
                #     score_sound.play()
                #     score_sound_countdown = 100
            else:
                screen.blit(game_over_surface, game_over_rect)
                high_score = update_score(score, high_score)
                # if lose is True:
                #     score_display('game_over')
                screen.blit(bird, bird_rect)
            #sàn
            floor_x_pos -= 1
            draw_floor()
            if floor_x_pos <= -800:
                floor_x_pos = 0

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE and game_active:
                        bird_movement = -4
                        flap_sound.play()
                    if event.key == pygame.K_SPACE and game_active == False:
                        game_active = True
                        pipe_list.clear()
                        bird_rect.center = (100, 300)
                        bird_movement = 0
                        score = 0
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1 and game_active:
                        bird_movement = -4
                        flap_sound.play()
                    if event.button == 1 and game_active == False:
                        game_active = True
                        pipe_list.clear()
                        bird_rect.center = (100, 300)
                        bird_movement = 0
                        score = 0
                if event.type == spawnpipe:
                    pipe_list.extend(create_pipe())

                    # print( "x= ",pipe_list[0].x)
                    # print( "right= ",pipe_list[0].right)
                    # print( "bird_rect.left= ",bird_rect.left)
                    # print( "bird_rect.x= ",bird_rect.x)
                    # print(pipe_list)
                    # if pipe_list[0].x < bird_rect.right :
                if event.type == birdflap:
                    if bird_index < 2:
                        bird_index += 1
                    else:
                        bird_index = 0
                    bird, bird_rect = bird_animation()

            pygame.display.update()
            clock.tick(60)
