import pygame


class Auth:
    login_success = False
    full_name = ""
    access_token = ""
    refresh_token = ""


class Color:
    bg_main = "#8DE3E6"
    text_color_red = "#EF3220"


class Font:
    main_font = "Cambria"


class Api:
    api_endpoint = "https://ever-study-api.onrender.com"


class FileUrl:
    f_toan_chuong_01 = "Toan_Chuong_01_Bieu_thuc,phan_thuc_dai_so.pdf"
    f_toan_chuong_02 = "Toan_Chuong_02_Cac_hinh_khoi_trong_thuc_tien.pdf"
    f_toan_chuong_03 = "Toan_Chuong_03_Dinh_li_Pythagore_cac_loai_tu_giac_thuong_gap.pdf"
    f_toan_chuong_04 = "Toan_Chuong_04_Thong_ke.pdf"
    f_toan_chuong_05 = "Toan_Chuong_05_Ham_so_va_do_thi.pdf"
    f_toan_chuong_06 = "Toan_Chuong_06_Phuong_trinh.pdf"
    f_toan_chuong_07 = "Toan_Chuong_07_Đinh_li_Thales.pdf"
    f_toan_chuong_08 = "Toan_Chuong_08_Tam_giac_dong_dang.pdf"
    f_toan_chuong_09 = "Toan_Chuong_09_Xac_suat.pdf"


class ImageUrl:
    # Background image
    bg_home_screen = "image/background/home.gif"
    bg_learn_screen = "image/background/on-tap.gif"
    bg_math_screen = "image/background/mon-toan.gif"
    bg_calculate_screen = "image/background/home-tinh-diem.gif"
    bg_subject_average = "image/background/tinh-diem-1.gif"
    bg_academic_result = "image/background/tinh-diem-2.gif"
    bg_game_screen = "image/background/q-a-1.gif"
    bg_discovery_screen = "image/background/hoc-tap.gif"
    bg_share_screen = "image/background/chia-se.gif"
    bg_other_screen = "image/background/tinh-diem-1.gif"
    bg_author_screen = "image/background/tac-gia.gif"
    bg_login_screen = "image/background/login.gif"

    app_icon = "image/ever-study.ico"


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
