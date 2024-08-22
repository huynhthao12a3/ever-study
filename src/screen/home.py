import pygame

from src.screen.author import AuthorScreen
from src.screen.calculate import CalculateScreen
from src.screen.game import GameScreen
from src.screen.learn import LearnScreen
from src.screen.other import OtherScreen
from src.utils.constant import InfoRect, Auth
from src.utils.file import FileManager
from src.utils.popup import ErasablePopup


class HomeScreen:
    def __init__(self, main_instance):
        print("Init learn screen")
        main_instance.is_home_screen = True
        main_instance.frames = FileManager().load_gif("image/background/home.gif")
        main_instance.frame_index = 0

    def draw_header_info(self, main_instance):
        if len(Auth.full_name) > 0:
            main_instance.popups[1] = ErasablePopup(main_instance.popup_font, "")
            main_instance.right_info_rect = pygame.draw.rect(main_instance.screen, (255, 255, 255), pygame.Rect(710, 4, 88, 30), InfoRect.width, InfoRect.border_radius)
        else:
            main_instance.popups[1] = ErasablePopup(main_instance.popup_font, "Đăng nhập")
            main_instance.right_info_rect = pygame.draw.rect(main_instance.screen, InfoRect.color, pygame.Rect(710, 4, 88, 30), InfoRect.width, InfoRect.border_radius)
        main_instance.popups[0].draw_at(main_instance.screen, (8, 4))
        main_instance.popups[1].draw_at(main_instance.screen, (720, 8))

    def run(self, main_instance, mouse_x, mouse_y):
        print("Home screen run", type(main_instance))
        print(mouse_x, mouse_y)
        if 150 < mouse_x < 370 and 240 < mouse_y < 350:  # Learn
            main_instance.set_false_all_screen()
            main_instance.learn_screen_instance = LearnScreen(main_instance)
        if 430 < mouse_x < 645 and 240 < mouse_y < 350:  # Calculate
            main_instance.set_false_all_screen()
            main_instance.calculate_screen_instance = CalculateScreen(main_instance)
        if 150 < mouse_x < 370 and 390 < mouse_y < 500:  # Game
            main_instance.set_false_all_screen()
            main_instance.game_screen_instance = GameScreen(main_instance)
        if 430 < mouse_x < 645 and 390 < mouse_y < 500:  # Other
            main_instance.set_false_all_screen()
            main_instance.other_screen_instance = OtherScreen(main_instance)
        if 370 < mouse_x < 650 and 555 < mouse_y < 600:  # Author
            main_instance.set_false_all_screen()
            main_instance.author_screen_instance = AuthorScreen(main_instance)