import pygame
import random
import sys
import time


class AnimalWordSearch:
    def __init__(self):
        pygame.init()
        self.WIDTH, self.HEIGHT = 800, 600
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Animal Word Search")

        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)
        self.RED = (255, 0, 0)
        self.GREEN = (0, 255, 0)
        self.YELLOW = (255, 255, 0)

        self.font = pygame.font.Font(None, 36)
        self.small_font = pygame.font.Font(None, 24)

        self.animals = ["CAT", "DOG", "LION", "TIGER", "ELEPHANT"]
        self.grid_size = 10
        self.grid = [[' ' for _ in range(self.grid_size)] for _ in range(self.grid_size)]

        self.game_time = 180  # 3 minutes
        self.start_time = time.time()
        self.score = 0

        self.current_word = ""
        self.found_words = set()

        self.clock = pygame.time.Clock()
        self.running = True

    def place_word(self, word):
        directions = [(0, 1), (1, 0), (1, 1), (-1, 1)]
        max_attempts = 100

        for _ in range(max_attempts):
            direction = random.choice(directions)
            dx, dy = direction

            if direction == (0, 1):
                x = random.randint(0, self.grid_size - 1)
                y = random.randint(0, self.grid_size - len(word))
            elif direction == (1, 0):
                x = random.randint(0, self.grid_size - len(word))
                y = random.randint(0, self.grid_size - 1)
            else:
                x = random.randint(max(0, -dx * (len(word) - 1)),
                                   min(self.grid_size - 1, self.grid_size - 1 - dx * (len(word) - 1)))
                y = random.randint(0, self.grid_size - len(word))

            if all(0 <= x + i * dx < self.grid_size and 0 <= y + i * dy < self.grid_size and
                   self.grid[y + i * dy][x + i * dx] in [' ', word[i]] for i in range(len(word))):
                for i in range(len(word)):
                    self.grid[y + i * dy][x + i * dx] = word[i]
                return True

        return False

    def initialize_grid(self):
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
        cell_size = 40
        for y in range(self.grid_size):
            for x in range(self.grid_size):
                pygame.draw.rect(self.screen, self.WHITE, (x * cell_size, y * cell_size, cell_size, cell_size), 1)
                letter = self.font.render(self.grid[y][x], True, self.WHITE)
                self.screen.blit(letter, (x * cell_size + 10, y * cell_size + 10))

    def draw_word_list(self):
        for i, word in enumerate(self.animals):
            color = self.GREEN if word in self.found_words else self.WHITE
            text = self.font.render(word, True, color)
            self.screen.blit(text, (self.grid_size * 40 + 20, i * 40))

    def find_word_positions(self, word):
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
        time_text = self.small_font.render(f"Time: {remaining_time}s", True, self.WHITE)
        score_text = self.small_font.render(f"Score: {self.score}", True, self.WHITE)
        self.screen.blit(time_text, (self.WIDTH - 100, 10))
        self.screen.blit(score_text, (self.WIDTH - 100, 30))

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
                elif event.key == pygame.K_RETURN:
                    if self.current_word.upper() in self.animals and self.current_word.upper() not in self.found_words:
                        self.found_words.add(self.current_word.upper())
                        self.score += len(self.current_word) * 10
                        print(f"Word found: {self.current_word}")
                    self.current_word = ""
                elif event.key == pygame.K_BACKSPACE:
                    self.current_word = self.current_word[:-1]
                else:
                    self.current_word += event.unicode.upper()

    def run(self):
        words_placed = self.initialize_grid()
        print(f"Words successfully placed: {words_placed}")

        try:
            while self.running:
                self.handle_events()

                self.screen.fill(self.BLACK)
                self.draw_grid()
                self.draw_word_list()
                self.draw_time_and_score()

                for word in self.found_words:
                    for positions in self.find_word_positions(word):
                        for x, y in positions:
                            pygame.draw.rect(self.screen, self.GREEN, (x * 40, y * 40, 40, 40), 3)

                input_text = self.font.render(self.current_word, True, self.WHITE)
                self.screen.blit(input_text, (10, self.HEIGHT - 40))

                pygame.display.flip()
                self.clock.tick(60)

                if time.time() - self.start_time >= self.game_time:
                    print("Time's up!")
                    self.running = False

        except Exception as e:
            print(f"An error occurred: {e}")

        finally:
            print(f"Game over! Final score: {self.score}")
            pygame.quit()
            sys.exit()


if __name__ == "__main__":
    game = AnimalWordSearch()
    game.run()
