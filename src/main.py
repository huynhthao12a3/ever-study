import pygame
from src.login import Login

class EverStudy:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption('Ôn luyện Toán 6')

        icon = pygame.image.load('./assets/image/setting/apple.png')
        pygame.display.set_icon(icon)

        pygame.display.flip()

    def run(self):
        Login()