import sys

import pygame
from src.login import Login
from src.utils.constant import Auth
from src.utils.file import FileManager
from src.utils.popup import ErasablePopup


class EverStudy:
    def __init__(self):
        # Pygame config
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

        # Current Screen
        self.is_home_screen = True
        self.is_learn_screen = False
        self.is_game_screen = False
        self.is_calculate_screen = False

        # Message Text For Displaying
        self.popup_font = pygame.font.SysFont("roboto", 14)
        self.popups = []  # list of popup objects
        self.hover_rects = []  # list of hover locations
        self.do_once = True
        self.popups.append(ErasablePopup(self.popup_font, ""))
        self.popups.append(ErasablePopup(self.popup_font, "Đăng nhập"))
        pygame.draw.rect(self.screen, (255, 0, 0), pygame.Rect(710, 4, 88, 30), 2, 10)

    def main(self):
        while True:
            # self.screen.blit(self.font.render(Auth.full_name, False, (0, 0, 0)), (4, 4))

            # Paint the background, but just once
            # if self.do_once:
            #     self.do_once = False
            #     for i in range(len(self.hover_rects)):
            #         pygame.draw.rect(self.screen, (255, 0, 0), self.hover_rects[i], 2)

            # Show information
            # print("len: ",len(self.popups))
            if len(self.popups) > 0:
                if self.is_home_screen is True and self.do_once is True:
                    self.do_once = False
                    self.popups[0].draw_at(self.screen, (8, 4))
                    self.popups[1].draw_at(self.screen, (720, 8))
                    print("home screen")

                # if self.is_home_screen is False and self.do_once is True:
                # self.do_once = False
                # self.popups[0].draw_at(self.screen, (8, 4))
                # self.popups[1].draw_at(self.screen, (720, 8))
                # print("other screen")

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
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    print("Click: ", mouse_x, mouse_y)
                    if event.button == 1 and self.is_home_screen is True:
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
                            # self.author()
                            Login(self.screen, self.popups, ErasablePopup)
                            self.do_once = True

            pygame.display.flip()

    pygame.quit()

    def learn(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        self.is_home_screen = False
        self.do_once = True
        # self.do_once = False

        print("other screen")
        print("learn", mouse_x, mouse_y)
        self.screen.blit(FileManager().load_image("image/background/hoc-tap.png"), (0, 0))
        self.draw_info()

    def calculate(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        self.is_home_screen = False
        print("calculate", mouse_x, mouse_y)
        self.screen.blit(FileManager().load_image("image/background/hoc-tap.png"), (0, 0))
        self.draw_info()

    def game(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        self.is_home_screen = False
        print("game", mouse_x, mouse_y)
        self.screen.blit(FileManager().load_image("image/background/hoc-tap.png"), (0, 0))
        self.draw_info()

    def other(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        self.is_home_screen = False
        print("other", mouse_x, mouse_y)
        self.screen.blit(FileManager().load_image("image/background/hoc-tap.png"), (0, 0))
        self.draw_info()

    def author(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        # self.is_home_screen = False
        print("author", mouse_x, mouse_y)
        # self.screen.blit(FileManager().load_image("image/background/hoc-tap.png"), (0, 0))

        self.draw_info()

    # Draw information and back button
    def draw_info(self):
        self.popups[1] = ErasablePopup(self.popup_font, "<- Trở về")
        pygame.draw.rect(self.screen, (0,0,0), pygame.Rect(720, 4, 78, 28), 2,10)
        self.popups[0].draw_at(self.screen, (8, 4))
        self.popups[1].draw_at(self.screen, (730, 8))

    def login(self):
        Login()
