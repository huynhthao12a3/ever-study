import random
import sys
import time

import pygame

from src.utils.constant import GameFlappyBird, Font, Question
from src.utils.file import FileManager
from src.utils.question import QuestionManager


class ClickableArea:
    def __init__(self, rect):
        self.rect = pygame.Rect(rect)


class FlappyBird:
    def __init__(self, on_flappy_bird_close, selected_subject):

        pygame.mixer.pre_init(frequency=44100, size=-16, channels=2, buffer=512)
        pygame.init()
        pygame.display.set_caption('Flappy Bird')
        self.screen = pygame.display.set_mode((800, 600))
        self.clock = pygame.time.Clock()
        self.game_font = pygame.font.SysFont(Font.main_font, 35)

        # Callback
        self.on_flappy_bird_close = on_flappy_bird_close
        self.game_result = {
            "game_score": 0,
            "answered_question": 0,
            "correct_answer": 0,
            "wrong_answer": 0
        }

        # Create variable
        self.gravity = 0.25
        self.bird_movement = 0
        self.game_active = False
        self.score = 0
        self.high_score = 0
        self.lose = False
        self.running = True
        self.scored = False
        self.collision = False
        self.wrong_answer_count = 0
        self.max_wrong_answers = 3

        # Question - answer
        self.question_manager = QuestionManager(Question)
        self.question_manager.set_mode(selected_subject)
        self.show_question = False
        self.current_question = None
        self.correct_answer = None
        self.selected_answer = None

        # Random bird, background, pipe
        self.random_bird = GameFlappyBird.img_bird[random.randint(0, len(GameFlappyBird.img_bird) - 1)]
        self.random_bg = GameFlappyBird.img_background[random.randint(0, len(GameFlappyBird.img_background) - 1)]
        self.random_pipe = GameFlappyBird.img_pipe[random.randint(0, len(GameFlappyBird.img_pipe) - 1)]

        # Create background
        self.file_manager = FileManager()
        self.bg = self.file_manager.load_image(self.random_bg, True)
        self.bg = pygame.transform.scale(self.bg, (800, 600))
        self.bg_x_pos = 0

        # Create floor
        self.floor = self.file_manager.load_image('image/flappy-bird/floor.png', True)
        self.floor_x_pos = 0

        # Create bird
        self.bird_down = self.file_manager.load_image(self.random_bird["bird_down"], True)
        self.bird_mid = self.file_manager.load_image(self.random_bird["bird_mid"], True)
        self.bird_up = self.file_manager.load_image(self.random_bird["bird_up"], True)
        self.bird_list = [self.bird_down, self.bird_mid, self.bird_up]  # 0 1 2
        self.bird_index = 0
        self.bird = self.bird_list[self.bird_index]
        self.bird_rect = self.bird.get_rect(center=(80, 300))

        # Create timer
        self.bird_flap = pygame.USEREVENT + 1
        pygame.time.set_timer(self.bird_flap, 200)

        # Create Pipe
        self.pipe_surface = self.file_manager.load_image(self.random_pipe, True)
        self.pipe_list = []

        # Create timer
        self.spawn_pipe = pygame.USEREVENT
        pygame.time.set_timer(self.spawn_pipe, 1000)
        self.pipe_height = [300, 320, 350, 380, 400]

        # Game over
        self.game_over_surface = pygame.transform.scale2x(
            self.file_manager.load_image('image/flappy-bird/message.png', True))
        self.game_over_rect = self.game_over_surface.get_rect(center=(400, 250))

        # Add sound
        self.flap_sound = pygame.mixer.Sound(self.file_manager.resource_path('sound/flappy-bird/sfx_wing.wav'))
        self.hit_sound = pygame.mixer.Sound(self.file_manager.resource_path('sound/flappy-bird/sfx_hit.wav'))
        self.score_sound = pygame.mixer.Sound(self.file_manager.resource_path('sound/flappy-bird/sfx_point.wav'))
        self.score_sound_countdown = 100

        # Click Area
        self.clickable_areas = [
            ClickableArea((50, 470, 120, 120)),   # A
            ClickableArea((240, 470, 120, 120)),  # B
            ClickableArea((435, 470, 125, 120)),  # C
            ClickableArea((630, 470, 120, 120))   # D
        ]

        # Cursor hand
        self.hand_cursor = pygame.cursors.Cursor(pygame.SYSTEM_CURSOR_HAND)
        self.default_cursor = pygame.cursors.Cursor(pygame.SYSTEM_CURSOR_ARROW)

    def draw_background(self):
        self.screen.blit(self.bg, (self.bg_x_pos, 0))
        self.screen.blit(self.bg, (self.bg_x_pos + 800, 0))

    def draw_floor(self):
        self.screen.blit(self.floor, (self.floor_x_pos, 500))
        self.screen.blit(self.floor, (self.floor_x_pos + 800, 500))

    def create_pipe(self):
        self.random_pipe_pos = random.choice(self.pipe_height)
        self.top_pipe = self.pipe_surface.get_rect(midtop=(800, self.random_pipe_pos - 440))
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
                self.scored = False
                self.collision = True
                self.show_question = True
                # Random question
                subject, question = self.question_manager.get_random_question()
                print(subject, question)
                self.current_question = question["image_path"]
                self.correct_answer = question["correct_answer"]
                return False
        if self.bird_rect.top <= -50 or self.bird_rect.bottom >= 520:
            self.hit_sound.play()
            self.lose = True
            self.scored = False
            self.collision = True
            self.show_question = True
            # Random question
            subject, question = self.question_manager.get_random_question()
            print(subject, question)
            self.current_question = question["image_path"]
            self.correct_answer = question["correct_answer"]
            return False

        return True

    def rotate_bird(self, bird1):
        new_bird = pygame.transform.rotozoom(bird1, -self.bird_movement * 1, 1)
        return new_bird

    def bird_animation(self):
        new_bird = self.bird_list[self.bird_index]
        new_bird_rect = new_bird.get_rect(center=(100, self.bird_rect.centery))
        return new_bird, new_bird_rect

    def score_display(self):
            score_surface = self.game_font.render(f'Điểm: {int(self.score)}', True, (255, 255, 255))
            score_rect = score_surface.get_rect(center=(70, 20))
            self.screen.blit(score_surface, score_rect)

    def display_question(self, image_path):
        self.screen.blit(self.file_manager.load_image(image_path, True), (0, 0))

    def answer_correct(self):
        font = pygame.font.Font(None, 36)
        text = font.render("Câu trả lời đúng", True, (255, 255, 255))
        text_rect = text.get_rect(center=(400, 300))
        self.screen.blit(text, text_rect)

        pygame.display.update()
        pygame.time.set_timer(self.spawn_pipe, 5000)
        time.sleep(5)
        pygame.time.set_timer(self.spawn_pipe, 1000)

        self.collision = False
        self.game_active = True
        self.bird_movement = -12

    def handle_mouse_click(self, pos):
        for i, area in enumerate(self.clickable_areas):
            if area.rect.collidepoint(pos):
                self.selected_answer = ["A", "B", "C", "D"][i]
                print(f"Selected answer: {self.selected_answer}")
                break

    def handle_mouse_motion(self, pos):
        cursor_changed = False
        for area in self.clickable_areas:
            if area.rect.collidepoint(pos):
                pygame.mouse.set_cursor(self.hand_cursor)
                cursor_changed = True
                break

        if not cursor_changed:
            pygame.mouse.set_cursor(self.default_cursor)

    def run(self):
        while self.running:
            # self.screen.blit(self.bg, (0, 0))

            # Draw background
            self.bg_x_pos -= 1
            self.draw_background()
            if self.bg_x_pos <= -800:
                self.bg_x_pos = 0

            # Calculate score
            if len(self.pipe_list) > 0:
                if self.pipe_list[0].x < self.bird_rect.centerx and self.scored is False:
                    self.score_sound.play()
                    self.score += 1
                    self.game_result["game_score"] += 1
                    self.scored = True
                if self.pipe_list[0].x < -100:
                    self.pipe_list.pop(0)
                    self.pipe_list.pop(0)
                    self.scored = False

            # Flappy Bird running
            if self.game_active is True and self.collision is False:
                # Bird
                self.bird_movement += self.gravity
                rotated_bird = self.rotate_bird(self.bird)
                self.bird_rect.centery += self.bird_movement
                self.screen.blit(rotated_bird, self.bird_rect)
                self.game_active = self.check_collision(self.pipe_list)
                # Pipe
                self.pipe_list = self.move_pipe(self.pipe_list)
                self.draw_pipe(self.pipe_list)
                # if self.collision is False:
                self.score_display()

                # Draw floor
                self.floor_x_pos -= 1
                self.draw_floor()
                if self.floor_x_pos <= -800:
                    self.floor_x_pos = 0
            else:
                self.scored = False
                self.pipe_list.clear()
                # self.screen.blit(self.game_over_surface, self.game_over_rect)
                # self.high_score = self.update_score(self.score, self.high_score)
                # if lose is True:
                self.score_display()
                self.bird_rect.center = (100, 300)
                self.screen.blit(self.bird, self.bird_rect)

                # Draw floor
                self.floor_x_pos -= 1
                self.draw_floor()
                if self.floor_x_pos <= -800:
                    self.floor_x_pos = 0

                # Bird collided pipe => Show question
                if self.collision is True: # and self.wrong_answer_count < self.max_wrong_answers:
                    # Show question
                    self.display_question(self.current_question)
                    # self.show_question = False

            # Pygame event
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    self.on_flappy_bird_close(self.game_result)  # Quit game

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.running = False
                        self.on_flappy_bird_close(self.game_result)  # Quit game

                    if event.key == pygame.K_SPACE and self.game_active:
                        self.bird_movement = -4
                        self.flap_sound.play()
                    if event.key == pygame.K_SPACE and self.game_active is False and self.collision is False:
                        self.game_active = True
                        # self.collision = False
                        # self.pipe_list.clear()
                        self.bird_rect.center = (100, 300)
                        self.bird_movement = 0
                        # self.score = 0

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    print(mouse_x, mouse_y)
                    if event.button == 1 and self.game_active:
                        self.bird_movement = -4
                        self.flap_sound.play()
                    if event.button == 1 and self.game_active is False and self.collision is False:
                        self.game_active = True
                        # self.collision = False
                        # self.pipe_list.clear()
                        self.bird_rect.center = (100, 300)
                        self.bird_movement = 0

                        # self.score = 0

                    # Bird collided pipe => choose answer
                    if event.button == 1 and self.collision is True:
                        print("Correct answer is ", self.correct_answer)
                        self.handle_mouse_click(event.pos)
                        # if 50 < mouse_x < 170 and 470 < mouse_y < 590:
                        #     self.selected_answer = "A"
                        # if 240 < mouse_x < 360 and 470 < mouse_y < 590:
                        #     self.selected_answer = "B"
                        # if 435 < mouse_x < 560 and 470 < mouse_y < 590:
                        #     self.selected_answer = "C"
                        # if 630 < mouse_x < 750 and 470 < mouse_y < 590:
                        #     self.selected_answer = "D"

                        if self.selected_answer is not None and self.selected_answer == self.correct_answer:
                            # increase answered question
                            self.game_result["answered_question"] += 1
                            self.game_result["correct_answer"] += 1

                            print("True: ", self.selected_answer, self.correct_answer)
                            font = pygame.font.SysFont(Font.main_font, 24)
                            text = font.render("Câu trả lời chính xác. Sẽ quay lại game sau 3 giây.", True, (255, 0, 0))
                            text_rect = text.get_rect(center=(400, 450))
                            self.screen.blit(text, text_rect)
                            pygame.display.update()

                            pygame.time.set_timer(self.spawn_pipe, 3000)  # Create pipe after 3s sleep
                            time.sleep(3)
                            pygame.time.set_timer(self.spawn_pipe, 1000)  # Rollback create pipe

                            self.collision = False
                            self.game_active = True
                            self.bird_movement = -12

                        if self.selected_answer is not None and self.selected_answer != self.correct_answer:
                            # increase answered question
                            self.wrong_answer_count += 1
                            self.game_result["answered_question"] += 1
                            self.game_result["wrong_answer"] += 1

                            if self.wrong_answer_count >= self.max_wrong_answers:
                                font = pygame.font.SysFont(Font.main_font, 24)
                                text = font.render("Game Over! Bạn đã sai đủ ba lần.", True, (255, 0, 0))
                                text_rect = text.get_rect(center=(400, 450))
                                self.screen.blit(text, text_rect)
                                pygame.display.update()
                                time.sleep(3)

                                self.collision = False
                                self.game_active = False
                                self.wrong_answer_count = 0
                                self.game_result["game_score"] += self.score
                                self.score = 0

                            else:
                                font = pygame.font.SysFont(Font.main_font, 24)
                                text = font.render("Câu trả lời không chính xác.", True, (255, 0, 0))
                                text_rect = text.get_rect(center=(400, 450))
                                self.screen.blit(text, text_rect)
                                pygame.display.update()
                                time.sleep(1)

                                # Hiển thị câu hỏi mới nếu chưa đạt số lần sai tối đa.
                                subject, question = self.question_manager.get_random_question()
                                if question:
                                    print("Câu hỏi mới:", subject)
                                    self.current_question = question["image_path"]
                                    self.correct_answer = question["correct_answer"]

                        self.selected_answer = None  # Reset answer

                elif event.type == pygame.MOUSEMOTION:
                    if self.collision is True:
                        self.handle_mouse_motion(event.pos)

                # Create pipe each second
                if event.type == self.spawn_pipe and self.game_active is True and self.collision is False:
                    self.pipe_list.extend(self.create_pipe())

                # Bird flap each 200ms
                if event.type == self.bird_flap:
                    if self.bird_index < 2:
                        self.bird_index += 1
                    else:
                        self.bird_index = 0
                    self.bird, self.bird_rect = self.bird_animation()
            # self.check_click_area()
            pygame.display.update()
            self.clock.tick(60)
        pygame.quit()

    def check_click_area(self):
        # Check click area
        if self.collision:
            for area in self.clickable_areas:
                pygame.draw.rect(self.screen, (255, 0, 0), area.rect, 2)
