import pygame
import random
import sys

from src.utils.constant import Font
from src.utils.file import FileManager

class AppleCatcher:
    def __init__(self, on_apple_catcher_close):
        pygame.mixer.pre_init(frequency=44100, size=-16, channels=2, buffer=512)
        pygame.init()
        self.width = 800
        self.height = 600
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption('Hứng Táo')
        self.clock = pygame.time.Clock()
        self.game_font = pygame.font.SysFont(Font.main_font, 35)
        self.large_font = pygame.font.SysFont(Font.main_font, 70)

        self.file_manager = FileManager()

        # Callback
        self.on_apple_catcher_close = on_apple_catcher_close
        self.game_result = {
            "game_score": 1,
            "answered_question": 2,
            "correct_answer": 3,
            "wrong_answer": 4,
        }

        # Biến trò chơi
        self.score = 0
        self.high_score = 0
        self.lives = 5
        self.level = 1
        self.game_active = False
        self.running = True
        self.game_over = False

        # Người chơi (giỏ)
        self.player_width = 100
        self.player_height = 50
        self.player_x = self.width // 2 - self.player_width // 2
        self.player_y = self.height - self.player_height - 10

        # Táo
        self.apple_size = 30
        self.apples = []
        self.spawn_apple = pygame.USEREVENT
        pygame.time.set_timer(self.spawn_apple, random.randint(800, 1500))

        # Tải hình ảnh
        self.bg = self.load_and_scale_image('image/apple-catcher/background.png', (self.width, self.height))
        self.basket = self.load_and_scale_image('image/apple-catcher/bat.png', (self.player_width, self.player_height))
        self.apple_image = self.load_and_scale_image('image/apple-catcher/apple.png', (self.apple_size, self.apple_size))
        self.heart_image = self.load_and_scale_image('image/apple-catcher/heart.png', (25, 25))

        # Tải âm thanh
        self.catch_sound = pygame.mixer.Sound(self.file_manager.resource_path('sound/flappy-bird/sfx_point.wav'))
        self.miss_sound = pygame.mixer.Sound(self.file_manager.resource_path('sound/flappy-bird/sfx_hit.wav'))
        self.game_over_sound = pygame.mixer.Sound(self.file_manager.resource_path('sound/flappy-bird/sfx_die.wav'))

    def load_and_scale_image(self, path, size):
        image = self.file_manager.load_image(path, True)
        return pygame.transform.scale(image, size)

    def create_apple(self):
        return {
            'rect': pygame.Rect(random.randint(0, self.width - self.apple_size), -self.apple_size, self.apple_size, self.apple_size),
            'speed': random.uniform(2 + self.level * 0.5, 5 + self.level * 0.5),
            'rotation': 0,
            'rotation_speed': random.uniform(-3, 3)
        }

    def move_apples(self):
        for apple in self.apples[:]:
            apple['rect'].y += apple['speed']
            apple['rect'].x += random.uniform(-0.5, 0.5)
            apple['rotation'] += apple['rotation_speed']
            if apple['rect'].top > self.height:
                self.apples.remove(apple)
                self.lives -= 1
                self.miss_sound.play()
                if self.lives <= 0:
                    self.game_over = True
                    self.game_over_sound.play()

    def check_collision(self):
        player_rect = pygame.Rect(self.player_x, self.player_y, self.player_width, self.player_height)
        for apple in self.apples[:]:
            if player_rect.colliderect(apple['rect']):
                self.apples.remove(apple)
                self.score += 1
                self.catch_sound.play()
                if self.score % 10 == 0:
                    self.level += 1

    def draw_objects(self):
        self.screen.blit(self.bg, (0, 0))
        self.screen.blit(self.basket, (self.player_x, self.player_y))
        for apple in self.apples:
            rotated_apple = pygame.transform.rotate(self.apple_image, apple['rotation'])
            rect = rotated_apple.get_rect(center=apple['rect'].center)
            self.screen.blit(rotated_apple, rect)

    def draw_ui(self):
        score_surface = self.game_font.render(f'Điểm: {self.score}', True, (0, 0, 0))
        level_surface = self.game_font.render(f'Cấp độ: {self.level}', True, (0, 0, 0))
        self.screen.blit(score_surface, (10, 10))
        self.screen.blit(level_surface, (10, 50))
        for i in range(self.lives):
            self.screen.blit(self.heart_image, (self.width - 35 - i * 30, 10))

    def draw_game_over(self):
        overlay = pygame.Surface((self.width, self.height))
        overlay.set_alpha(128)
        overlay.fill((0, 0, 0))
        self.screen.blit(overlay, (0, 0))
        game_over_text = self.large_font.render('Game Over', True, (255, 0, 0))
        score_text = self.game_font.render(f'Điểm cuối cùng: {self.score}', True, (255, 255, 255))
        restart_text = self.game_font.render('Nhấn SPACE để chơi lại', True, (255, 255, 255))
        self.screen.blit(game_over_text, (self.width // 2 - game_over_text.get_width() // 2, self.height // 2 - 100))
        self.screen.blit(score_text, (self.width // 2 - score_text.get_width() // 2, self.height // 2))
        self.screen.blit(restart_text, (self.width // 2 - restart_text.get_width() // 2, self.height // 2 + 100))

    def reset_game(self):
        self.score = 0
        self.lives = 5
        self.level = 1
        self.apples.clear()
        self.game_over = False
        self.game_active = False

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    self.on_apple_catcher_close(self.game_result)  # Quit game
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.running = False
                        self.on_apple_catcher_close(self.game_result)  # Quit game
                    if event.key == pygame.K_SPACE and self.game_over:
                        self.reset_game()
                if event.type == self.spawn_apple and self.game_active and not self.game_over:
                    self.apples.append(self.create_apple())
                    pygame.time.set_timer(self.spawn_apple, random.randint(800 - self.level * 50, 1500 - self.level * 50))
                if event.type == pygame.MOUSEBUTTONDOWN and not self.game_active:
                    self.game_active = True

            if self.game_active and not self.game_over:
                mouse_x, _ = pygame.mouse.get_pos()
                self.player_x = mouse_x - self.player_width // 2
                self.player_x = max(0, min(self.player_x, self.width - self.player_width))

                self.move_apples()
                self.check_collision()

            self.screen.fill((255, 255, 255))
            self.draw_objects()
            self.draw_ui()

            if self.game_over:
                self.draw_game_over()

            pygame.display.update()
            self.clock.tick(60)

        pygame.quit()

if __name__ == "__main__":
    game = AppleCatcher()
    game.run()