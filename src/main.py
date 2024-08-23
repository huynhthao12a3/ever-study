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

        # Init gif
        self.frames = FileManager().load_gif("image/background/home.gif")
        self.frame_index = 0
        self.clock = pygame.time.Clock()
        self.pygame_image = FileManager().pil_image_to_pygame_surface(self.frames[self.frame_index])

        self.font = pygame.font.SysFont("roboto", 18)

        # Current Screen
        self.is_home_screen = True
        self.is_learn_screen = False
        self.is_game_screen = False
        self.is_calculate_screen = False
        self.is_other_screen = False
        self.is_author_screen = False

        # Instance
        self.home_screen_instance = HomeScreen(self)
        self.learn_screen_instance = None
        self.game_screen_instance = None
        self.calculate_screen_instance = None
        self.other_screen_instance = None
        self.author_screen_instance = None

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

            if len(self.popups) > 0:
                if self.is_home_screen is True:
                    print("home screen")
                    self.home_screen_instance.draw_header_info(self)

                if self.is_learn_screen is True:
                    print("learn screen")
                    self.learn_screen_instance.draw_header_info(self)

                if self.is_calculate_screen is True:
                    print("Calculate screen")
                    self.calculate_screen_instance.draw_header_info(self)

                if self.is_game_screen is True:
                    # print("game screen")
                    self.game_screen_instance.draw_header_info(self)

                if self.is_other_screen is True:
                    print("other screen")
                    self.other_screen_instance.draw_header_info(self)

                if self.is_author_screen is True:
                    print("author screen")
                    self.author_screen_instance.draw_header_info(self)

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
                    if event.button == 1:
                        mouse_x, mouse_y = pygame.mouse.get_pos()  # Get mouse position
                        if self.right_info_rect.collidepoint(mouse_x, mouse_y):
                            if self.is_home_screen is True:
                                print("click đăng nhập")
                                Login(self)
                            if (self.is_learn_screen is True or self.is_calculate_screen is True
                                    or self.is_game_screen is True or self.is_other_screen is True
                                    or self.is_author_screen is True):
                                print("Click trở về")
                                self.set_false_all_screen()
                                self.home_screen_instance = HomeScreen(self)

                        if self.is_home_screen is True:
                            self.home_screen_instance.run(self, mouse_x, mouse_y)

                        if self.is_game_screen is True:
                            # print("game screen")
                            print(mouse_x, mouse_y)
                            self.game_screen_instance.run(self, mouse_x, mouse_y)

            pygame.display.flip()

    pygame.quit()

    def set_false_all_screen(self):
        self.is_home_screen = False
        self.is_learn_screen = False
        self.is_game_screen = False
        self.is_calculate_screen = False
        self.is_other_screen = False
        self.is_author_screen = False
