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
    bg_game_screen = "image/background/chon-tro-choi.gif"
    bg_utility_screen = "image/background/tien-ich.gif"
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


class Question:
    math = [
        {
            "image_path": "image/question/toan_cauhoi01_B.png",
            "correct_answer": "image/question/toan_cauhoi01_B.png".split(".")[0][-1]  # correct answer
        },
        {
            "image_path": "image/question/toan_cauhoi02_B.png",
            "correct_answer": "image/question/toan_cauhoi02_B.png".split(".")[0][-1]  # correct answer
        },
        {
            "image_path": "image/question/toan_cauhoi03_A.png",
            "correct_answer": "image/question/toan_cauhoi03_A.png".split(".")[0][-1]  # correct answer
        },
        {
            "image_path": "image/question/toan_cauhoi04_A.png",
            "correct_answer": "image/question/toan_cauhoi04_A.png".split(".")[0][-1]  # correct answer
        },
        {
            "image_path": "image/question/toan_cauhoi05_B.png",
            "correct_answer": "image/question/toan_cauhoi05_B.png".split(".")[0][-1]  # correct answer
        },
        {
            "image_path": "image/question/toan_cauhoi06_D.png",
            "correct_answer": "image/question/toan_cauhoi06_D.png".split(".")[0][-1]  # correct answer
        },
        {
            "image_path": "image/question/toan_cauhoi07_A.png",
            "correct_answer": "image/question/toan_cauhoi07_A.png".split(".")[0][-1]  # correct answer
        },
        {
            "image_path": "image/question/toan_cauhoi08_A.png",
            "correct_answer": "image/question/toan_cauhoi08_A.png".split(".")[0][-1]  # correct answer
        },
        {
            "image_path": "image/question/toan_cauhoi9_D.png",
            "correct_answer": "image/question/toan_cauhoi9_D.png".split(".")[0][-1]  # correct answer
        },
        {
            "image_path": "image/question/toan_cauhoi10_B.png",
            "correct_answer": "image/question/toan_cauhoi10_B.png".split(".")[0][-1]  # correct answer
        }
    ]
    computer_science = [
        {
            "image_path": "image/question/tinhoc_cauhoi01_A.png",
            "correct_answer": "image/question/tinhoc_cauhoi01_A.png".split(".")[0][-1]  # correct answer
        },
        {
            "image_path": "image/question/tinhoc_cauhoi02_A.png",
            "correct_answer": "image/question/tinhoc_cauhoi02_A.png".split(".")[0][-1]  # correct answer
        },
        {
            "image_path": "image/question/tinhoc_cauhoi03_D.png",
            "correct_answer": "image/question/tinhoc_cauhoi03_D.png".split(".")[0][-1]  # correct answer
        },
        {
            "image_path": "image/question/tinhoc_cauhoi04_B.png",
            "correct_answer": "image/question/tinhoc_cauhoi04_B.png".split(".")[0][-1]  # correct answer
        },
    ]
    english = [
        {
            "image_path": "image/question/tienganh_cauhoi01_C.png",
            "correct_answer": "image/question/tienganh_cauhoi01_C.png".split(".")[0][-1]  # correct answer
        },
        {
            "image_path": "image/question/tienganh_cauhoi02_A.png",
            "correct_answer": "image/question/tienganh_cauhoi02_A.png".split(".")[0][-1]  # correct answer
        },
        {
            "image_path": "image/question/tienganh_cauhoi03_A.png",
            "correct_answer": "image/question/tienganh_cauhoi03_A.png".split(".")[0][-1]  # correct answer
        },
        {
            "image_path": "image/question/tienganh_cauhoi04_A.png",
            "correct_answer": "image/question/tienganh_cauhoi04_A.png".split(".")[0][-1]  # correct answer
        },
    ]
    literature = [
        {
            "image_path": "image/question/nguvan_cauhoi1_B.png",
            "correct_answer": "image/question/nguvan_cauhoi1_B.png".split(".")[0][-1]  # correct answer
        },
        {
            "image_path": "image/question/nguvan_cauhoi02_C.png",
            "correct_answer": "image/question/nguvan_cauhoi02_C.png".split(".")[0][-1]  # correct answer
        },
        {
            "image_path": "image/question/nguvan_cauhoi03_C.png",
            "correct_answer": "image/question/nguvan_cauhoi03_C.png".split(".")[0][-1]  # correct answer
        },
    ]
    history_geography = [
        {
            "image_path": "image/question/lsdl_cauhoi01_A.png",
            "correct_answer": "image/question/lsdl_cauhoi01_A.png".split(".")[0][-1]  # correct answer
        },
        {
            "image_path": "image/question/lsdl_cauhoi02_D.png",
            "correct_answer": "image/question/lsdl_cauhoi02_D.png".split(".")[0][-1]  # correct answer
        },
        {
            "image_path": "image/question/lsdl_cauhoi03_C.png",
            "correct_answer": "image/question/lsdl_cauhoi03_C.png".split(".")[0][-1]  # correct answer
        },
        {
            "image_path": "image/question/lsdl_cauhoi04_B.png",
            "correct_answer": "image/question/lsdl_cauhoi04_B.png".split(".")[0][-1]  # correct answer
        },
        {
            "image_path": "image/question/lsdl_cauhoi05_ C.png",
            "correct_answer": "image/question/lsdl_cauhoi05_ C.png".split(".")[0][-1]  # correct answer
        },
        {
            "image_path": "image/question/lsdl_cauhoi06_B.png",
            "correct_answer": "image/question/lsdl_cauhoi06_B.png".split(".")[0][-1]  # correct answer
        },
        {
            "image_path": "image/question/lsdl_cauhoi07_D.png",
            "correct_answer": "image/question/lsdl_cauhoi07_D.png".split(".")[0][-1]  # correct answer
        },
        {
            "image_path": "image/question/lsdl_cauhoi08_A.png",
            "correct_answer": "image/question/lsdl_cauhoi08_A.png".split(".")[0][-1]  # correct answer
        }
    ]
    natural_sciences = [
        {
            "image_path": "image/question/khtn_cauhoi01_A.png",
            "correct_answer": "image/question/khtn_cauhoi01_A.png".split(".")[0][-1]  # correct answer
        },
        {
            "image_path": "image/question/khtn_cauhoi02_B.png",
            "correct_answer": "image/question/khtn_cauhoi02_B.png".split(".")[0][-1]  # correct answer
        },
        {
            "image_path": "image/question/khtn_cauhoi03_C.png",
            "correct_answer": "image/question/khtn_cauhoi03_C.png".split(".")[0][-1]  # correct answer
        },
        {
            "image_path": "image/question/khtn_cauhoi04_C.png",
            "correct_answer": "image/question/khtn_cauhoi04_C.png".split(".")[0][-1]  # correct answer
        },
    ]
    civic_education = [
        {
            "image_path": "image/question/giaoduccongdan_cauhoi01_A.png",
            "correct_answer": "image/question/giaoduccongdan_cauhoi01_A.png".split(".")[0][-1]  # correct answer
        },
        {
            "image_path": "image/question/giaoduccongdan_cauhoi02_C.png",
            "correct_answer": "image/question/giaoduccongdan_cauhoi02_C.png".split(".")[0][-1]  # correct answer
        },
        {
            "image_path": "image/question/giaoduccongdan_cauhoi03_C.png",
            "correct_answer": "image/question/giaoduccongdan_cauhoi03_C.png".split(".")[0][-1]  # correct answer
        },
        {
            "image_path": "image/question/giaoduccongdan_cauhoi04_A.png",
            "correct_answer": "image/question/giaoduccongdan_cauhoi04_A.png".split(".")[0][-1]  # correct answer
        },
    ]
    technology = [
        {
            "image_path": "image/question/congnghe_cauhoi01_D.png",
            "correct_answer": "image/question/congnghe_cauhoi01_D.png".split(".")[0][-1]  # correct answer
        },
        {
            "image_path": "image/question/congnghe_cauhoi02_A.png",
            "correct_answer": "image/question/congnghe_cauhoi02_A.png".split(".")[0][-1]  # correct answer
        },
        {
            "image_path": "image/question/congnghe_cauhoi03_A.png",
            "correct_answer": "image/question/congnghe_cauhoi03_A.png".split(".")[0][-1]  # correct answer
        },
        {
            "image_path": "image/question/congnghe_cauhoi04_B.png",
            "correct_answer": "image/question/congnghe_cauhoi04_B.png".split(".")[0][-1]  # correct answer
        },
    ]


class GameConfig:
    selected_subject = None  # All & (Math or History or ...)
    selected_game = None  # Flappy_Bird or Apple_Catcher or Animal_Word_Search
    selected_level = None  # 1 or 2 or 3 or 4

