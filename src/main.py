import sys

import pygame
from src.screen.login import Login
from src.screen.author import AuthorScreen
from src.screen.calculate import CalculateScreen
from src.screen.game import GameScreen
from src.screen.home import HomeScreen
from src.screen.other import OtherScreen
from src.utils.file import FileManager
from src.utils.popup import ErasablePopup
from src.screen.learn import LearnScreen


class EverStudy:
    def __init__(self):
        # Pygame config
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption('Ever Study')

        icon = FileManager().load_image('image/setting/apple.png', True)
        pygame.display.set_icon(icon)

        # background = FileManager().load_image("image/background/home.png", True)
        # self.screen.blit(background, (0, 0))
        # Init gif
        self.frames = FileManager().load_gif("image/background/home.gif")
        self.frame_index = 0
        self.clock = pygame.time.Clock()
        self.pygame_image = FileManager().pil_image_to_pygame_surface(self.frames[self.frame_index])
        # print(pygame.font.get_fonts())

        self.font = pygame.font.SysFont("roboto", 18)
        # self.screen.blit(self.font.render("Login", True, (0, 0, 0)), (4, 4))

        # Current Screen
        self.is_home_screen = True
        self.is_learn_screen = False
        self.is_game_screen = False
        self.is_calculate_screen = False
        self.is_other_screen = False
        self.is_author_screen = False

        self.home_screen = HomeScreen(self)
        self.learn_screen = None
        self.game_screen = None
        self.calculate_screen = None
        self.other_screen = None
        self.author_screen = None

        self.left_info_rect = None
        self.right_info_rect = None

        # Message Text For Displaying
        self.popup_font = pygame.font.SysFont("roboto", 14)
        self.popups = []  # list of popup objects
        self.hover_rects = []  # list of hover locations
        self.do_once = True
        self.popups.append(ErasablePopup(self.popup_font, ""))
        self.popups.append(ErasablePopup(self.popup_font, "Đăng nhập"))

    def main(self):
        while True:
            # Load gif
            self.pygame_image = FileManager().pil_image_to_pygame_surface(self.frames[self.frame_index])
            self.screen.blit(self.pygame_image, (0, 0))
            self.frame_index = (self.frame_index + 1) % len(self.frames)
            self.clock.tick(10)
            # self.screen.blit(self.font.render(Auth.full_name, False, (0, 0, 0)), (4, 4))

            # Paint the background, but just once
            # if self.do_once:
            #     self.do_once = False
            #     for i in range(len(self.hover_rects)):
            #         pygame.draw.rect(self.screen, (255, 0, 0), self.hover_rects[i], 2)

            # Show information
            # print("len: ",len(self.popups))
            if len(self.popups) > 0:
                if self.is_home_screen is True:
                    print("home screen")
                    self.home_screen.draw_header_info(self)

                if self.is_learn_screen is True:
                    print("learn screen")
                    self.learn_screen.draw_header_info(self)

                if self.is_calculate_screen is True:
                    print("Calculate screen")
                    self.calculate_screen.draw_header_info(self)

                if self.is_game_screen is True:
                    print("game screen")
                    self.game_screen.draw_header_info(self)

                if self.is_other_screen is True:
                    print("other screen")
                    self.other_screen.draw_header_info(self)

                if self.is_author_screen is True:
                    print("author screen")
                    self.author_screen.draw_header_info(self)

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
                    if event.button == 1:
                        if self.right_info_rect.collidepoint(mouse_x, mouse_y):
                            if self.is_home_screen is True:
                                print("click đăng nhập")
                                Login(self)
                            if (self.is_learn_screen is True or self.is_calculate_screen is True
                                    or self.is_game_screen is True or self.is_other_screen is True
                                    or self.is_author_screen is True):
                                print("Click trở về")
                                self.set_false_all_screen()
                                self.home_screen = HomeScreen(self)
                        if self.is_home_screen is True:
                            mouse_x, mouse_y = pygame.mouse.get_pos()  # Get mouse position

                            if 150 < mouse_x < 370 and 240 < mouse_y < 350:  # Learn
                                self.set_false_all_screen()
                                self.learn_screen = LearnScreen(self)
                            if 430 < mouse_x < 645 and 240 < mouse_y < 350:  # Calculate
                                self.set_false_all_screen()
                                self.calculate_screen = CalculateScreen(self)
                            if 150 < mouse_x < 370 and 390 < mouse_y < 500:  # Game
                                self.set_false_all_screen()
                                self.game_screen = GameScreen(self)
                            if 430 < mouse_x < 645 and 390 < mouse_y < 500:  # Other
                                self.set_false_all_screen()
                                self.other_screen = OtherScreen(self)
                            if 370 < mouse_x < 650 and 555 < mouse_y < 600:  # Author
                                self.set_false_all_screen()
                                self.author_screen = AuthorScreen(self)

                        if self.is_learn_screen is True:
                            print("learning screen")

            pygame.display.flip()

    pygame.quit()

    def home(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        self.current_screen("home")
        self.home_screen = HomeScreen(self)
        # self.frames = FileManager().load_gif("image/background/hoc-tap.gif")
        # self.frame_index = 0
        # self.draw_info()

    def learn(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        self.current_screen("learn")
        self.learn_screen = LearnScreen(self)
        # self.frames = FileManager().load_gif("image/background/hoc-tap.gif")
        # self.frame_index = 0
        # self.draw_info()

    def calculate(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        self.current_screen("calculate")
        self.calculate_screen = CalculateScreen(self)
        # print("calculate", mouse_x, mouse_y)
        # self.screen.blit(FileManager().load_image("image/background/hoc-tap.png"), (0, 0))
        # self.draw_info()

    def game(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        self.current_screen("game")
        self.game_screen = GameScreen(self)
        # print("game", mouse_x, mouse_y)
        # self.screen.blit(FileManager().load_image("image/background/hoc-tap.png"), (0, 0))
        # self.draw_info()

    def other(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        self.current_screen("other")
        self.other_screen = OtherScreen(self)
        # print("other", mouse_x, mouse_y)
        # self.screen.blit(FileManager().load_image("image/background/hoc-tap.png"), (0, 0))
        # self.draw_info()

    def author(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        self.current_screen("author")
        self.author_screen = AuthorScreen(self)
        # print("author", mouse_x, mouse_y)
        # self.screen.blit(FileManager().load_image("image/background/hoc-tap.png"), (0, 0))
        # self.draw_info()

    # Draw information and back button
    def draw_info(self):
        self.popups[1] = ErasablePopup(self.popup_font, "<- Trở về")
        pygame.draw.rect(self.screen, (0, 0, 0), pygame.Rect(720, 4, 78, 28), 2, 10)
        self.popups[0].draw_at(self.screen, (8, 4))
        self.popups[1].draw_at(self.screen, (730, 8))

    def set_false_all_screen(self):
        self.is_home_screen = False
        self.is_learn_screen = False
        self.is_game_screen = False
        self.is_calculate_screen = False
        self.is_other_screen = False
        self.is_author_screen = False
        # image_path = "image/background/home.gif"
        # if screen_name == "home":
        #     self.is_home_screen = True
        #     image_path = "image/background/home.gif"
        # if screen_name == "learn":
        #     self.is_learn_screen = True
        #     image_path = "image/background/hoc-tap.gif"
        # if screen_name == "game":
        #     self.is_game_screen = True
        #     image_path = "image/background/game.gif"
        # if screen_name == "calculate":
        #     self.is_calculate_screen = True
        #     image_path = "image/background/home-tinh-diem.gif"
        # if screen_name == "author":
        #     self.is_author_screen = True
        #     image_path = "image/background/q-a-1.gif"
        # if screen_name == "other":
        #     self.is_other_screen = True
        #     image_path = "image/background/q-a-1.gif"
        #
        # self.frames = FileManager().load_gif(image_path)
        # self.frame_index = 0
        # self.draw_info()

    def login(self):
        Login()
