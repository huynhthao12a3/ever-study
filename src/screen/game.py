import pygame

from src.utils.constant import InfoRect
from src.utils.file import FileManager
from src.utils.popup import ErasablePopup


class GameScreen:
    def __init__(self, main_instance):
        print("Init game screen")
        main_instance.is_game_screen = True
        main_instance.frames = FileManager().load_gif("image/background/game.png")
        main_instance.frame_index = 0

    def draw_header_info(self, main_instance):
        main_instance.popups[1] = ErasablePopup(main_instance.popup_font, "<- Trở về")
        main_instance.right_info_rect = pygame.draw.rect(main_instance.screen, InfoRect.color, InfoRect.rect, InfoRect.width, InfoRect.border_radius)
        main_instance.popups[0].draw_at(main_instance.screen, (8, 4))
        main_instance.popups[1].draw_at(main_instance.screen, (730, 8))
