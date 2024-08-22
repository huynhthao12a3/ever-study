import pygame

from src.utils.constant import InfoRect, Auth
from src.utils.file import FileManager
from src.utils.popup import ErasablePopup


class HomeScreen:
    def __init__(self, home_screen):
        print("Init learn screen")
        home_screen.is_home_screen = True
        home_screen.frames = FileManager().load_gif("image/background/home.gif")
        home_screen.frame_index = 0

    def draw_header_info(self, home_screen):
        if len(Auth.full_name) > 0:
            home_screen.popups[1] = ErasablePopup(home_screen.popup_font, "")
            home_screen.right_info_rect = pygame.draw.rect(home_screen.screen, (255, 255, 255), pygame.Rect(710, 4, 88, 30), InfoRect.width, InfoRect.border_radius)
        else:
            home_screen.popups[1] = ErasablePopup(home_screen.popup_font, "Đăng nhập")
            home_screen.right_info_rect = pygame.draw.rect(home_screen.screen, InfoRect.color, pygame.Rect(710, 4, 88, 30), InfoRect.width, InfoRect.border_radius)
        home_screen.popups[0].draw_at(home_screen.screen, (8, 4))
        home_screen.popups[1].draw_at(home_screen.screen, (720, 8))
