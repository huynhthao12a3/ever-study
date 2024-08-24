import pygame


class Auth:
    login_success = False
    full_name = ""
    access_token = ""
    refresh_token = ""


class InfoRect:
    color = (255, 0, 0)
    rect = pygame.Rect(720, 4, 78, 28)
    width = 2
    border_radius = 10


class Api:
    api_endpoint = "https://ever-study.onrender.com"
