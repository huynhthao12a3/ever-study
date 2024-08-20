import sys

import pygame
from src.login import Login
from src.utils.constant import Auth
from src.utils.file import FileManager


class EverStudy:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption('Ever Study')

        icon = FileManager().load_image('image/setting/apple.png', True)
        pygame.display.set_icon(icon)

        background = FileManager().load_image("image/background/home.png", True)
        self.screen.blit(background, (0, 0))

        # print(pygame.font.get_fonts())

        self.font = pygame.font.SysFont("roboto", 18)
        # self.screen.blit(self.font.render("Login", True, (0, 0, 0)), (4, 4))

        self.home = True

    def main(self):
        while True:
            self.screen.blit(self.font.render(Auth.full_name, False, (0, 0, 0)), (4, 4))

            for event in pygame.event.get():
                # Quit
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()

                # Mouse click
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # Home screen
                    if event.button == 1 and self.home is True:
                        mouse_x, mouse_y = pygame.mouse.get_pos()  # Get mouse position
                        # print("Click: ", mouse_x, mouse_y)
                        if 150 < mouse_x < 370 and 240 < mouse_y < 350:  # Learn
                            self.learn()
                        if 430 < mouse_x < 645 and 240 < mouse_y < 350:  # Calculate
                            self.calculate()
                        if 150 < mouse_x < 370 and 390 < mouse_y < 500:  # Game
                            self.game()
                        if 430 < mouse_x < 645 and 390 < mouse_y < 500:  # Other
                            self.other()
                        if 370 < mouse_x < 650 and 555 < mouse_y < 600:  # Author
                            self.author()
                            Login()

            pygame.display.flip()

    pygame.quit()

    def learn(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        self.home = False
        print("learn", mouse_x, mouse_y)
        self.screen.blit(FileManager().load_image("image/background/hoc-tap.png"), (0, 0))

    def calculate(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        self.home = False
        print("calculate", mouse_x, mouse_y)
        self.screen.blit(FileManager().load_image("image/background/hoc-tap.png"), (0, 0))

    def game(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        self.home = False
        print("game", mouse_x, mouse_y)
        self.screen.blit(FileManager().load_image("image/background/hoc-tap.png"), (0, 0))

    def other(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        self.home = False
        print("other", mouse_x, mouse_y)
        self.screen.blit(FileManager().load_image("image/background/hoc-tap.png"), (0, 0))

    def author(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        self.home = False
        print("author", mouse_x, mouse_y)
        self.screen.blit(FileManager().load_image("image/background/hoc-tap.png"), (0, 0))

    def login(self):
        Login()
