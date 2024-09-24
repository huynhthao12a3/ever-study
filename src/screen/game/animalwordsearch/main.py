import pygame
import random
import sys
import time


class AnimalWordSearch:
    def __init__(self, on_animal_word_search_close):
        # Khởi tạo Pygame và cài đặt màn hình
        pygame.init()
        self.WIDTH, self.HEIGHT = 800, 600
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Animal Word Search")

        # Định nghĩa màu sắc
        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)
        self.RED = (255, 0, 0)
        self.GREEN = (0, 255, 0)
        self.YELLOW = (255, 255, 0)

        # Tạo font chữ
        self.font = pygame.font.SysFont('Roboto', 26)
        self.small_font = pygame.font.SysFont('Roboto', 18)

        # Danh sách các từ cần tìm
        self.animals = ["CAT", "DOG", "LION", "TIGER", "PIG"]
        self.grid_size = 10
        self.grid = [[' ' for _ in range(self.grid_size)] for _ in range(self.grid_size)]

        # Thiết lập thời gian và điểm số
        self.game_time = 180  # 3 phút
        self.start_time = time.time()
        self.score = 0

        # Biến để lưu từ đang nhập và các từ đã tìm thấy
        self.current_word = ""
        self.found_words = set()

        # Khởi tạo đồng hồ và biến chạy game
        self.clock = pygame.time.Clock()
        self.running = True

        # Callback
        self.on_animal_word_search_close = on_animal_word_search_close
        self.game_result = {
            "game_score": 1,
            "answered_question": 2,
            "correct_answer": 3,
            "wrong_answer": 4,
        }

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
        for word in self.animals:
            if self.place_word(word):
                words_placed.append(word)

        for y in range(self.grid_size):
            for x in range(self.grid_size):
                if self.grid[y][x] == ' ':
                    self.grid[y][x] = random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

        return words_placed

    def draw_grid(self):
        cell_size = 50  # Giả sử kích thước ô là 50x50 pixel
        for y in range(self.grid_size):
            for x in range(self.grid_size):
                # Vẽ ô
                pygame.draw.rect(self.screen, self.WHITE, (x * cell_size, y * cell_size, cell_size, cell_size), 1)
                # Render chữ
                letter = self.font.render(self.grid[y][x], True, self.WHITE)
                # Tính toán vị trí để đặt chữ vào giữa ô
                letter_x = x * cell_size + (cell_size - letter.get_width()) // 2
                letter_y = y * cell_size + (cell_size - letter.get_height()) // 2
                # Vẽ chữ
                self.screen.blit(letter, (letter_x, letter_y))

    def draw_word_list(self):
        # Vẽ danh sách các từ cần tìm
        for i, word in enumerate(self.animals):
            color = self.GREEN if word in self.found_words else self.WHITE
            text = self.font.render(word, True, color)
            self.screen.blit(text, (self.grid_size * 50 + 20, i * 40))

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
        # Hiển thị thời gian còn lại và điểm số
        elapsed_time = int(time.time() - self.start_time)
        remaining_time = max(0, self.game_time - elapsed_time)
        time_text = self.small_font.render(f"Time: {remaining_time}s", True, self.WHITE)
        score_text = self.small_font.render(f"Score: {self.score}", True, self.WHITE)
        self.screen.blit(time_text, (self.WIDTH - 100, 10))
        self.screen.blit(score_text, (self.WIDTH - 100, 30))

    def draw_input_box(self):
        # Vẽ ô nhập
        input_box = pygame.Rect(10, self.HEIGHT - 50, 300, 40)
        pygame.draw.rect(self.screen, self.WHITE, input_box, 2)
        input_text = self.font.render(self.current_word, True, self.WHITE)
        self.screen.blit(input_text, (input_box.x + 5, input_box.y + 5))

    def draw_background(self):
        # Vẽ background gradient lên màn hình
        for y in range(self.HEIGHT):
            # Tính toán màu sắc cho mỗi dòng
            color = (255 - int(y * 255 / self.HEIGHT), 150, int(y * 255 / self.HEIGHT))
            pygame.draw.line(self.screen, color, (0, y), (self.WIDTH, y))

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
                    if self.current_word.upper() in self.animals and self.current_word.upper() not in self.found_words:
                        self.found_words.add(self.current_word.upper())
                        self.score += len(self.current_word) * 10
                        print(f"Word found: {self.current_word}")
                    self.current_word = ""
                elif event.key == pygame.K_BACKSPACE:
                    self.current_word = self.current_word[:-1]
                else:
                    # Giới hạn độ dài của từ nhập vào
                    if len(self.current_word) < 15:  # Độ dài tối đa là 10 ký tự
                        self.current_word += event.unicode.upper()

    def run(self):
        # Vòng lặp chính của game
        words_placed = self.initialize_grid()
        print(f"Words successfully placed: {words_placed}")

        try:
            while self.running:
                self.handle_events()

                # self.screen.fill(self.BLACK)
                self.draw_background()
                self.draw_grid()
                self.draw_word_list()
                self.draw_time_and_score()

                # Highlight các từ đã tìm thấy
                for word in self.found_words:
                    for positions in self.find_word_positions(word):
                        for x, y in positions:
                            pygame.draw.rect(self.screen, self.GREEN, (x * 50, y * 50, 50, 50), 3)

                # Hiển thị từ đang nhập
                # input_text = self.font.render(self.current_word, True, self.WHITE)
                # self.screen.blit(input_text, (10, self.HEIGHT - 40))
                self.draw_input_box()

                pygame.display.flip()
                self.clock.tick(60)

                # Kiểm tra thời gian
                if time.time() - self.start_time >= self.game_time:
                    print("Time's up!")
                    self.running = False

        except Exception as e:
            print(f"An error occurred: {e}")

        finally:
            print(f"Game over! Final score: {self.score}")
            pygame.quit()


def on_animal_word_search_close(self):
    print("test")


if __name__ == "__main__":
    game = AnimalWordSearch(on_animal_word_search_close)
    game.run()
