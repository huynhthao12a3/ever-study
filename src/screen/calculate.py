import pygame

from src.utils.constant import InfoRect
from src.utils.file import FileManager
from src.utils.popup import ErasablePopup


class CalculateScreen:
    def __init__(self, home_screen):
        print("Init calculate screen")
        home_screen.is_calculate_screen = True
        home_screen.frames = FileManager().load_gif("image/background/home-tinh-diem.gif")
        home_screen.frame_index = 0

    def draw_header_info(self, home_screen):
        home_screen.popups[1] = ErasablePopup(home_screen.popup_font, "<- Trở về")
        home_screen.right_info_rect = pygame.draw.rect(home_screen.screen, InfoRect.color, InfoRect.rect, InfoRect.width, InfoRect.border_radius)
        home_screen.popups[0].draw_at(home_screen.screen, (8, 4))
        home_screen.popups[1].draw_at(home_screen.screen, (730, 8))
