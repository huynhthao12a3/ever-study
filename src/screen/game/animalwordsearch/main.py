from tkinter import messagebox

import pygame
import random
import sys
import time
from src.utils.constant import Font, GameWordSearch, ImageUrl
from src.utils.file import FileManager


class AnimalWordSearch:
    def __init__(self, on_animal_word_search_close, selected_subject, selected_level):
        # Khởi tạo Pygame và cài đặt màn hình
        pygame.init()
        self.WIDTH, self.HEIGHT = 800, 600
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Word Search")

        self.file_manager = FileManager()
        self.background = self.file_manager.load_image(ImageUrl.bg_word_search_screen)
        # self.background = pygame.transform.scale(self.background, (self.WIDTH, self.HEIGHT))

        # Định nghĩa màu sắc
        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)
        self.RED = (255, 0, 0)
        self.GREEN = (0, 255, 0)
        self.YELLOW = (255, 255, 0)

        # Tạo font chữ
        self.font = pygame.font.SysFont(Font.main_font, 26)
        self.small_font = pygame.font.SysFont(Font.main_font, 18)

        # Danh sách các từ cần tìm
        self.words = None
        self.grid_size = 10
        self.grid = [[' ' for _ in range(self.grid_size)] for _ in range(self.grid_size)]

        # Chọn ngẫu nhiên 5 từ
        if selected_subject == "math":
            self.words = random.sample(GameWordSearch.math[selected_level], 5)  # ["CAT", "DOG", "LION", "TIGER", "PIG"]
        elif selected_subject == "english":
            self.words = random.sample(GameWordSearch.english[selected_level], 5)
        else:
            self.words = random.sample(GameWordSearch.history[selected_level], 5)
        print(selected_subject, selected_level)
        print(self.words)

        # Thiết lập thời gian và điểm số
        self.game_time = 180  # 3 phút
        self.start_time = time.time()
        self.score = 0

        # Biến để lưu từ đang nhập và các từ đã tìm thấy
        self.current_word = ""
        self.found_words = set()
        self.revealed_words = set()

        # Khởi tạo đồng hồ và biến chạy game
        self.clock = pygame.time.Clock()
        self.running = True

        # Callback
        self.on_animal_word_search_close = on_animal_word_search_close
        self.game_result = {
            "game_score": 0,
            "answered_question": 0,
            "correct_answer": 0,
            "wrong_answer": 0,
        }

        self.cell_size = None

    def place_word(self, word):
        # Đặt một từ vào lưới theo hướng ngẫu nhiên
        # Định nghĩa các hướng có thể đặt từ (dọc, ngang, chéo xuống, chéo lên)
        directions = [(0, 1), (1, 0), (1, 1), (-1, 1)]
        # Số lần thử tối đa để đặt từ
        max_attempts = 100

        for _ in range(max_attempts):
            # Chọn ngẫu nhiên một hướng
            direction = random.choice(directions)
            dx, dy = direction

            # Xác định vị trí bắt đầu (x, y) cho từ dựa trên hướng
            if direction == (0, 1):  # Dọc
                x = random.randint(0, self.grid_size - 1)
                y = random.randint(0, self.grid_size - len(word))
            elif direction == (1, 0):  # Ngang
                x = random.randint(0, self.grid_size - len(word))
                y = random.randint(0, self.grid_size - 1)
            else:  # Chéo
                x = random.randint(max(0, -dx * (len(word) - 1)),
                                   min(self.grid_size - 1, self.grid_size - 1 - dx * (len(word) - 1)))
                y = random.randint(0, self.grid_size - len(word))

            # Kiểm tra xem từ có thể đặt được không
            if all(0 <= x + i * dx < self.grid_size and 0 <= y + i * dy < self.grid_size and
                   self.grid[y + i * dy][x + i * dx] in [' ', word[i]] for i in range(len(word))):
                # Nếu có thể đặt được, đặt từ vào lưới
                for i in range(len(word)):
                    self.grid[y + i * dy][x + i * dx] = word[i]
                return True  # Đặt thành công

        # Nếu không thể đặt sau max_attempts lần thử
        return False

    def initialize_grid(self):
        # Khởi tạo lưới với các từ và điền các ô trống bằng chữ cái ngẫu nhiên
        words_placed = []
        for word in self.words:
            if self.place_word(word):
                words_placed.append(word)

        for y in range(self.grid_size):
            for x in range(self.grid_size):
                if self.grid[y][x] == ' ':
                    self.grid[y][x] = random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

        return words_placed

    def draw_grid(self):
        self.cell_size = 40
        grid_width = self.grid_size * self.cell_size
        grid_height = self.grid_size * self.cell_size
        start_x = (self.WIDTH - grid_width) // 2
        start_y = (self.HEIGHT - grid_height) // 2 - 30  # Dịch lên trên 1 chút

        for y in range(self.grid_size):
            for x in range(self.grid_size):
                rect_x = start_x + x * self.cell_size
                rect_y = start_y + y * self.cell_size
                pygame.draw.rect(self.screen, self.WHITE, (rect_x, rect_y, self.cell_size, self.cell_size), 1)
                letter = self.font.render(self.grid[y][x], True, self.BLACK)
                letter_x = rect_x + (self.cell_size - letter.get_width()) // 2
                letter_y = rect_y + (self.cell_size - letter.get_height()) // 2
                self.screen.blit(letter, (letter_x, letter_y))

    def draw_word_list(self):
        word_list_y = (self.HEIGHT + self.grid_size * self.cell_size) // 2 + 20
        word_spacing = 20
        total_width = sum(self.font.size(word)[0] for word in self.words) + word_spacing * (len(self.words) - 1)
        start_x = (self.WIDTH - total_width) // 2

        for word in self.words:
            if word in self.revealed_words:
                color = self.GREEN if word in self.found_words else self.BLACK
                text = self.font.render(word, True, color)
                self.screen.blit(text, (start_x, word_list_y))
                start_x += text.get_width() + word_spacing
            else:
                text = self.font.render("?" * len(word), True, self.BLACK)
                self.screen.blit(text, (start_x, word_list_y))
                start_x += text.get_width() + word_spacing

    def find_word_positions(self, word):
        # Tìm vị trí của một từ trong lưới
        positions = []
        for y in range(self.grid_size):
            for x in range(self.grid_size):
                for dx, dy in [(0, 1), (1, 0), (1, 1), (-1, 1)]:
                    if all(0 <= x + i * dx < self.grid_size and 0 <= y + i * dy < self.grid_size and
                           self.grid[y + i * dy][x + i * dx] == word[i] for i in range(len(word))):
                        positions.append([(x + i * dx, y + i * dy) for i in range(len(word))])
        return positions

    def draw_time_and_score(self):
        elapsed_time = int(time.time() - self.start_time)
        remaining_time = max(0, self.game_time - elapsed_time)
        time_text = self.small_font.render(f"Thời gian: {remaining_time} giây", True, self.BLACK)
        score_text = self.small_font.render(f"Điểm: {self.score}", True, self.BLACK)
        self.screen.blit(time_text, (10, 5))
        self.screen.blit(score_text, (720, 5))

    def draw_input_box(self):
        input_box_width = 300
        input_box_height = 40
        input_box_x = (self.WIDTH - input_box_width) // 2
        input_box_y = self.HEIGHT - 120
        input_box = pygame.Rect(input_box_x, input_box_y, input_box_width, input_box_height)

        # Vẽ hình chữ nhật trắng làm nền
        pygame.draw.rect(self.screen, self.WHITE, input_box)

        # Vẽ viền đen
        pygame.draw.rect(self.screen, self.BLACK, input_box, 2)

        input_text = self.font.render(self.current_word, True, self.BLACK)
        text_x = input_box_x + 5
        text_y = input_box_y + (input_box_height - input_text.get_height()) // 2
        self.screen.blit(input_text, (text_x, text_y))

    def draw_background(self):
        self.screen.blit(self.background, (0, 0))

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                self.on_animal_word_search_close(self.game_result)  # Quit game
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
                    self.on_animal_word_search_close(self.game_result)  # Quit game
                elif event.key == pygame.K_RETURN:
                    if self.current_word.upper() in self.words and self.current_word.upper() not in self.found_words:
                        self.found_words.add(self.current_word.upper())
                        self.revealed_words.add(self.current_word.upper())
                        self.score += len(self.current_word)
                        self.game_result['game_score'] = self.score
                        print(f"Word found: {self.current_word}")
                    self.current_word = ""
                elif event.key == pygame.K_BACKSPACE:
                    self.current_word = self.current_word[:-1]
                else:
                    # Giới hạn độ dài của từ nhập vào
                    if len(self.current_word) < 15:  # Độ dài tối đa là 10 ký tự
                        self.current_word += event.unicode.upper()

    def run(self):
        words_placed = self.initialize_grid()
        print(f"Words successfully placed: {words_placed}")

        try:
            while self.running:
                self.handle_events()

                self.draw_background()
                self.draw_grid()
                self.draw_word_list()
                self.draw_time_and_score()
                self.draw_input_box()

                # Highlight các từ đã tìm thấy
                for word in self.found_words:
                    for positions in self.find_word_positions(word):
                        for x, y in positions:
                            rect_x = (self.WIDTH - self.grid_size * self.cell_size) // 2 + x * self.cell_size
                            rect_y = (self.HEIGHT - self.grid_size * self.cell_size) // 2 - 30 + y * self.cell_size
                            pygame.draw.rect(self.screen, self.GREEN, (rect_x, rect_y, self.cell_size, self.cell_size), 3)

                pygame.display.flip()
                self.clock.tick(60)

                if len(self.found_words) == 5 or time.time() - self.start_time >= self.game_time:
                    messagebox.showinfo("Kết thúc trò chơi", f"Điểm số của bạn là: {self.score}.")
                    self.running = False

        except Exception as e:
            print(f"An error occurred: {e}")

        finally:
            print(f"Game over! Final score: {self.score}")
            self.on_animal_word_search_close(self.game_result)
            pygame.quit()

