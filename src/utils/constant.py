import pygame


class Auth:
    login_success = False
    full_name = ""
    access_token = ""
    refresh_token = ""


class Color:
    bg_main = "#C4E6EF"


class Api:
    api_endpoint = "https://ever-study-api.onrender.com"


class ImageUrl:
    # Background image
    bg_home_screen = "image/background/home.gif"
    bg_learn_screen = "image/background/hoc-tap.gif"
    bg_calculate_screen = "image/background/home-tinh-diem.gif"
    bg_subject_average = "image/background/tinh-diem-1.gif"
    bg_academic_result = "image/background/tinh-diem-2.gif"
    bg_game_screen = "image/background/q-a-1.gif"
    bg_discovery_screen = "image/background/hoc-tap.gif"
    bg_share_screen = "image/background/hoc-tap.gif"
    bg_other_screen = "image/background/tinh-diem-1.gif"
    bg_author_screen = "image/background/tinh-diem-2.gif"
    bg_login_screen = "image/background/login.gif"


class GameFlappyBird:
    img_bird = [
        {
            "bird_down": 'image/flappy-bird/yellowbird-downflap.png',
            "bird_mid": 'image/flappy-bird/yellowbird-midflap.png',
            "bird_up": 'image/flappy-bird/yellowbird-upflap.png',
        },
        {
            "bird_down": 'image/flappy-bird/bluebird-downflap.png',
            "bird_mid": 'image/flappy-bird/bluebird-midflap.png',
            "bird_up": 'image/flappy-bird/bluebird-upflap.png',
        },
        {
            "bird_down": 'image/flappy-bird/redbird-downflap.png',
            "bird_mid": 'image/flappy-bird/redbird-midflap.png',
            "bird_up": 'image/flappy-bird/redbird-upflap.png',
        }
    ]
    img_background = [
        'image/flappy-bird/background-night.png',
        'image/flappy-bird/background-day.png',
        'image/flappy-bird/background-sky-1.jpg',
        'image/flappy-bird/background-sky-2.jpg',
        'image/flappy-bird/background-sky-3.jpg',
        'image/flappy-bird/background-sky-4.jpg'
    ]
    img_pipe = [
        'image/flappy-bird/pipe-green.png',
        'image/flappy-bird/pipe-red.png'
    ]
    questions = {
        # Math
        "math_01": {
            "image_path": "image/background/q-a-1.gif",
            "correct_answer": "A"
        },
        "math_02": {
            "image_path": "image/background/q-a-1.gif",
            "correct_answer": "B"
        },
        "math_03": {
            "image_path": "image/background/q-a-1.gif",
            "correct_answer": "C"
        }
    }
