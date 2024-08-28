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
    api_endpoint = "https://ever-study-api.onrender.com"


class ImageUrl:
    # Background image
    bg_home_screen = "image/background/home.gif"
    bg_learn_screen = "image/background/hoc-tap.gif"
    bg_calculate_screen = "image/background/home-tinh-diem.gif"
    bg_game_screen = "image/background/q-a-1.gif"
    bg_discovery_screen = "image/background/hoc-tap.gif"
    bg_share_screen = "image/background/hoc-tap.gif"
    bg_other_screen = "image/background/tinh-diem-1.gif"
    bg_author_screen = "image/background/tinh-diem-2.gif"
    bg_login_screen = "image/background/login.gif"
    bg_subject_average = "image/background/tinh-diem-1.gif"
