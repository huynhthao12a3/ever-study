import pygame


class Auth:
    login_success = False
    full_name = ""
    access_token = ""
    refresh_token = ""


class Color:
    bg_main = "#8DE3E6"
    text_color_red = "#EF3220"
    bg_color_blue = "#F0FBFD"
    bg_color_yellow = "#FCFFB5"


class Font:
    main_font = "Cambria"
    main_font_12 = "Cambria 14"
    main_font_mold = "Cambria 16 bold"


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
    bg_time_table_screen = "image/background/tkb.png"
    bg_time_table_child1_screen = "image/background/tkb-1.gif"
    bg_time_table_child2_screen = "image/background/tkb-2.gif"
    bg_exam_screen = "image/background/tien-ich-thi.gif"
    bg_share_screen = "image/background/chia-se.gif"
    bg_other_screen = "image/background/tinh-diem-1.gif"
    bg_author_screen = "image/background/tac-gia.gif"
    bg_login_screen = "image/background/login.gif"
    bg_game_mode_screen = "image/background/chon-che-do-choi.gif"
    bg_normal_game_mode_screen = "image/background/choi-thuong.gif"
    bg_rank_screen = "image/background/bxh.gif"
    bg_word_search_mode_screen = "image/background/word-search-mode.gif"
    bg_word_search_screen = "image/background/word-search.png"

    # Icon
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


class GameWordSearch:
    math = {
        "lv1": ["TAPHOP", "PHANTU", "TINHCHAT", "SOTUNHIEN", "LUYTHUA", "SOMU", "COSO", "THUASO", "GIAOHOAN", "KETHOP"],
        "lv2": ["CHIAHET", "TANCUNG", "UOCCHUNG", "BOICHUNG", "SONGUYENTO", "HOPSO", "QUYDONG", "RUTGON", "MAYTINH", "NGOACTRON"],
        "lv3": ["CHIAHET", "TANCUNG", "UOCCHUNG", "BOICHUNG", "SONGUYENTO", "HOPSO", "QUYDONG", "RUTGON", "MAYTINH", "NGOACTRON"],
        "lv4": ["CHIAHET", "TANCUNG", "UOCCHUNG", "BOICHUNG", "SONGUYENTO", "HOPSO", "QUYDONG", "RUTGON", "MAYTINH", "NGOACTRON"]
    }
    english = {
        "lv1": ["DETEST", "FOND", "CRAZY", "MESSAGE", "PUZZLE", "LEISURE", "FOLD"],
        "lv2": ["DRY", "FEED", "MILK", "CATTLE", "HARVEST", "LOAD"],
        "lv3": ["CONNECT", "FORUM", "STRESS", "PRESSURE", "BROWSE", "ACCOUNT"],
        "lv4": ["CROP", "HIGHLAND", "SOIL", "MINORITY", "FOLK", "FEATURE"]
    }
    history = {
        "lv1": ["CACHMANG", "DOCTAI", "NGHIVIEN", "THUOCDIA", "GIAIPHONG", "QUYTOC", "CONGNGHIEP", "JAMESWATT", "KHAITHAC", "HOINUOC"],
        "lv2": ["XAMNHAP", "TUBAN", "CUONGBUC", "DOHO", "THUCDAN", "NGUDAN", "CONGNHAN", "DUONGSAT", "DONDIEN", "RUONGDAT"],
        "lv3": ["PHONGKIEN", "PHANTRANH", "XUNGDOT", "DANGNGOAI", "DANGTRONG", "NOICHIEN", "DAIVIET", "HOANGSA", "TRUONGSA", "KHAIHOANG"],
        "lv4": ["PHONGKIEN", "PHANTRANH", "XUNGDOT", "DANGNGOAI", "DANGTRONG", "NOICHIEN", "DAIVIET", "HOANGSA", "TRUONGSA", "KHAIHOANG"]
    }


class Question:
    math = [
        {
            "image_path": "image/question/game/toan_cauhoi01_B.png",
            "correct_answer": "image/question/game/toan_cauhoi01_B.png".split(".")[0][-1]  # correct answer
        },
        {
            "image_path": "image/question/game/toan_cauhoi02_C.png",
            "correct_answer": "image/question/game/toan_cauhoi02_C.png".split(".")[0][-1]  # correct answer
        },
        {
            "image_path": "image/question/game/toan_cauhoi03_A.png",
            "correct_answer": "image/question/game/toan_cauhoi03_A.png".split(".")[0][-1]  # correct answer
        },
        {
            "image_path": "image/question/game/toan_cauhoi04_A.png",
            "correct_answer": "image/question/game/toan_cauhoi04_A.png".split(".")[0][-1]  # correct answer
        },
        {
            "image_path": "image/question/game/toan_cauhoi05_A.png",
            "correct_answer": "image/question/game/toan_cauhoi05_A.png".split(".")[0][-1]  # correct answer
        },
        {
            "image_path": "image/question/game/toan_cauhoi06_D.png",
            "correct_answer": "image/question/game/toan_cauhoi06_D.png".split(".")[0][-1]  # correct answer
        },
        {
            "image_path": "image/question/game/toan_cauhoi07_C.png",
            "correct_answer": "image/question/game/toan_cauhoi07_C.png".split(".")[0][-1]  # correct answer
        },
        {
            "image_path": "image/question/game/toan_cauhoi08_C.png",
            "correct_answer": "image/question/game/toan_cauhoi08_C.png".split(".")[0][-1]  # correct answer
        },
        {
            "image_path": "image/question/game/toan_cauhoi9_D.png",
            "correct_answer": "image/question/game/toan_cauhoi9_D.png".split(".")[0][-1]  # correct answer
        },
        {
            "image_path": "image/question/game/toan_cauhoi10_B.png",
            "correct_answer": "image/question/game/toan_cauhoi10_B.png".split(".")[0][-1]  # correct answer
        }
    ]
    computer_science = [
        {
            "image_path": "image/question/game/tinhoc_cauhoi01_A.png",
            "correct_answer": "image/question/game/tinhoc_cauhoi01_A.png".split(".")[0][-1]  # correct answer
        },
        {
            "image_path": "image/question/game/tinhoc_cauhoi02_A.png",
            "correct_answer": "image/question/game/tinhoc_cauhoi02_A.png".split(".")[0][-1]  # correct answer
        },
        {
            "image_path": "image/question/game/tinhoc_cauhoi03_D.png",
            "correct_answer": "image/question/game/tinhoc_cauhoi03_D.png".split(".")[0][-1]  # correct answer
        },
        {
            "image_path": "image/question/game/tinhoc_cauhoi04_B.png",
            "correct_answer": "image/question/game/tinhoc_cauhoi04_B.png".split(".")[0][-1]  # correct answer
        },
    ]
    english = [
        {
            "image_path": "image/question/game/tienganh_cauhoi01_C.png",
            "correct_answer": "image/question/game/tienganh_cauhoi01_C.png".split(".")[0][-1]  # correct answer
        },
        {
            "image_path": "image/question/game/tienganh_cauhoi02_A.png",
            "correct_answer": "image/question/game/tienganh_cauhoi02_A.png".split(".")[0][-1]  # correct answer
        },
        {
            "image_path": "image/question/game/tienganh_cauhoi03_A.png",
            "correct_answer": "image/question/game/tienganh_cauhoi03_A.png".split(".")[0][-1]  # correct answer
        },
        {
            "image_path": "image/question/game/tienganh_cauhoi04_A.png",
            "correct_answer": "image/question/game/tienganh_cauhoi04_A.png".split(".")[0][-1]  # correct answer
        },
    ]
    literature = [
        {
            "image_path": "image/question/game/nguvan_cauhoi1_B.png",
            "correct_answer": "image/question/game/nguvan_cauhoi1_B.png".split(".")[0][-1]  # correct answer
        },
        {
            "image_path": "image/question/game/nguvan_cauhoi02_C.png",
            "correct_answer": "image/question/game/nguvan_cauhoi02_C.png".split(".")[0][-1]  # correct answer
        },
        {
            "image_path": "image/question/game/nguvan_cauhoi03_C.png",
            "correct_answer": "image/question/game/nguvan_cauhoi03_C.png".split(".")[0][-1]  # correct answer
        },
    ]
    history_geography = [
        {
            "image_path": "image/question/game/lsdl_cauhoi01_A.png",
            "correct_answer": "image/question/game/lsdl_cauhoi01_A.png".split(".")[0][-1]  # correct answer
        },
        {
            "image_path": "image/question/game/lsdl_cauhoi02_D.png",
            "correct_answer": "image/question/game/lsdl_cauhoi02_D.png".split(".")[0][-1]  # correct answer
        },
        {
            "image_path": "image/question/game/lsdl_cauhoi03_C.png",
            "correct_answer": "image/question/game/lsdl_cauhoi03_C.png".split(".")[0][-1]  # correct answer
        },
        {
            "image_path": "image/question/game/lsdl_cauhoi04_B.png",
            "correct_answer": "image/question/game/lsdl_cauhoi04_B.png".split(".")[0][-1]  # correct answer
        },
        {
            "image_path": "image/question/game/lsdl_cauhoi05_ C.png",
            "correct_answer": "image/question/game/lsdl_cauhoi05_ C.png".split(".")[0][-1]  # correct answer
        },
        {
            "image_path": "image/question/game/lsdl_cauhoi06_B.png",
            "correct_answer": "image/question/game/lsdl_cauhoi06_B.png".split(".")[0][-1]  # correct answer
        },
        {
            "image_path": "image/question/game/lsdl_cauhoi07_D.png",
            "correct_answer": "image/question/game/lsdl_cauhoi07_D.png".split(".")[0][-1]  # correct answer
        },
        {
            "image_path": "image/question/game/lsdl_cauhoi08_A.png",
            "correct_answer": "image/question/game/lsdl_cauhoi08_A.png".split(".")[0][-1]  # correct answer
        }
    ]
    natural_sciences = [
        {
            "image_path": "image/question/game/khtn_cauhoi01_A.png",
            "correct_answer": "image/question/game/khtn_cauhoi01_A.png".split(".")[0][-1]  # correct answer
        },
        {
            "image_path": "image/question/game/khtn_cauhoi02_B.png",
            "correct_answer": "image/question/game/khtn_cauhoi02_B.png".split(".")[0][-1]  # correct answer
        },
        {
            "image_path": "image/question/game/khtn_cauhoi03_C.png",
            "correct_answer": "image/question/game/khtn_cauhoi03_C.png".split(".")[0][-1]  # correct answer
        },
        {
            "image_path": "image/question/game/khtn_cauhoi04_C.png",
            "correct_answer": "image/question/game/khtn_cauhoi04_C.png".split(".")[0][-1]  # correct answer
        },
    ]
    civic_education = [
        {
            "image_path": "image/question/game/giaoduccongdan_cauhoi01_A.png",
            "correct_answer": "image/question/game/giaoduccongdan_cauhoi01_A.png".split(".")[0][-1]  # correct answer
        },
        {
            "image_path": "image/question/game/giaoduccongdan_cauhoi02_C.png",
            "correct_answer": "image/question/game/giaoduccongdan_cauhoi02_C.png".split(".")[0][-1]  # correct answer
        },
        {
            "image_path": "image/question/game/giaoduccongdan_cauhoi03_C.png",
            "correct_answer": "image/question/game/giaoduccongdan_cauhoi03_C.png".split(".")[0][-1]  # correct answer
        },
        {
            "image_path": "image/question/game/giaoduccongdan_cauhoi04_A.png",
            "correct_answer": "image/question/game/giaoduccongdan_cauhoi04_A.png".split(".")[0][-1]  # correct answer
        },
    ]
    technology = [
        {
            "image_path": "image/question/game/congnghe_cauhoi01_D.png",
            "correct_answer": "image/question/game/congnghe_cauhoi01_D.png".split(".")[0][-1]  # correct answer
        },
        {
            "image_path": "image/question/game/congnghe_cauhoi02_A.png",
            "correct_answer": "image/question/game/congnghe_cauhoi02_A.png".split(".")[0][-1]  # correct answer
        },
        {
            "image_path": "image/question/game/congnghe_cauhoi03_A.png",
            "correct_answer": "image/question/game/congnghe_cauhoi03_A.png".split(".")[0][-1]  # correct answer
        },
        {
            "image_path": "image/question/game/congnghe_cauhoi04_B.png",
            "correct_answer": "image/question/game/congnghe_cauhoi04_B.png".split(".")[0][-1]  # correct answer
        },
    ]


class Exam:
    ATGT = [
        {
            "image_path": "image/question/exam/ATGT_01_B.gif",
            "correct_answer": "image/question/exam/ATGT_01_B.gif".split(".")[0][-1],
            "A": "image/question/exam/ATGT_01_B.A.gif",
            "B": "image/question/exam/ATGT_01_B.B.gif",
            "C": "image/question/exam/ATGT_01_B.C.gif",
            "D": "image/question/exam/ATGT_01_B.D.gif",
        },
        {
            "image_path": "image/question/exam/ATGT_02_C.gif",
            "correct_answer": "image/question/exam/ATGT_02_C.gif".split(".")[0][-1],
            "A": "image/question/exam/ATGT_02_C.A.gif",
            "B": "image/question/exam/ATGT_02_C.B.gif",
            "C": "image/question/exam/ATGT_02_C.C.gif",
            "D": "image/question/exam/ATGT_02_C.D.gif",
        },
        {
            "image_path": "image/question/exam/ATGT_03_B.gif",
            "correct_answer": "image/question/exam/ATGT_03_B.gif".split(".")[0][-1],
            "A": "image/question/exam/ATGT_03_B.A.gif",
            "B": "image/question/exam/ATGT_03_B.B.gif",
            "C": "image/question/exam/ATGT_03_B.C.gif",
            "D": "image/question/exam/ATGT_03_B.D.gif",
        },{
            "image_path": "image/question/exam/ATGT_04_C.gif",
            "correct_answer": "image/question/exam/ATGT_04_C.gif".split(".")[0][-1],
            "A": "image/question/exam/ATGT_04_C.A.gif",
            "B": "image/question/exam/ATGT_04_C.B.gif",
            "C": "image/question/exam/ATGT_04_C.C.gif",
            "D": "image/question/exam/ATGT_04_C.D.gif",
        },
        {
            "image_path": "image/question/exam/ATGT_05_B.gif",
            "correct_answer": "image/question/exam/ATGT_05_B.gif".split(".")[0][-1],
            "A": "image/question/exam/ATGT_05_B.A.gif",
            "B": "image/question/exam/ATGT_05_B.B.gif",
            "C": "image/question/exam/ATGT_05_B.C.gif",
            "D": "image/question/exam/ATGT_05_B.D.gif",
        }
    ]
    BLHD = [
        {
            "image_path": "image/question/exam/BLHĐ_01_C.gif",
            "correct_answer": "image/question/exam/BLHĐ_01_C.gif".split(".")[0][-1],
            "A": "image/question/exam/BLHĐ_01_C.A.gif",
            "B": "image/question/exam/BLHĐ_01_C.B.gif",
            "C": "image/question/exam/BLHĐ_01_C.C.gif",
            "D": "image/question/exam/BLHĐ_01_C.D.gif",
        },
        {
            "image_path": "image/question/exam/BLHĐ_02_B.gif",
            "correct_answer": "image/question/exam/BLHĐ_02_B.gif".split(".")[0][-1],
            "A": "image/question/exam/BLHĐ_02_B.A.gif",
            "B": "image/question/exam/BLHĐ_02_B.B.gif",
            "C": "image/question/exam/BLHĐ_02_B.C.gif",
            "D": "image/question/exam/BLHĐ_02_B.D.gif",
        },
        {
            "image_path": "image/question/exam/BLHĐ_03_B.gif",
            "correct_answer": "image/question/exam/BLHĐ_03_B.gif".split(".")[0][-1],
            "A": "image/question/exam/BLHĐ_03_B.A.gif",
            "B": "image/question/exam/BLHĐ_03_B.B.gif",
            "C": "image/question/exam/BLHĐ_03_B.C.gif",
            "D": "image/question/exam/BLHĐ_03_B.D.gif",
        },
    ]
    XHTD = [
        {
            "image_path": "image/question/exam/XHTD_01_B.gif",
            "correct_answer": "image/question/exam/XHTD_01_B.gif".split(".")[0][-1],
            "A": "image/question/exam/XHTD_01_B.A.gif",
            "B": "image/question/exam/XHTD_01_B.B.gif",
            "C": "image/question/exam/XHTD_01_B.C.gif",
            "D": "image/question/exam/XHTD_01_B.D.gif",
        },
        {
            "image_path": "image/question/exam/XHTD_02_B.gif",
            "correct_answer": "image/question/exam/XHTD_02_B.gif".split(".")[0][-1],
            "A": "image/question/exam/XHTD_02_B.A.gif",
            "B": "image/question/exam/XHTD_02_B.B.gif",
            "C": "image/question/exam/XHTD_02_B.C.gif",
            "D": "image/question/exam/XHTD_02_B.D.gif",
        },
        {
            "image_path": "image/question/exam/XHTD_03_C.gif",
            "correct_answer": "image/question/exam/XHTD_03_C.gif".split(".")[0][-1],
            "A": "image/question/exam/XHTD_03_C.A.gif",
            "B": "image/question/exam/XHTD_03_C.B.gif",
            "C": "image/question/exam/XHTD_03_C.C.gif",
            "D": "image/question/exam/XHTD_03_C.D.gif",
        },
        {
            "image_path": "image/question/exam/XHTD_04_B.gif",
            "correct_answer": "image/question/exam/XHTD_04_B.gif".split(".")[0][-1],
            "A": "image/question/exam/XHTD_04_B.A.gif",
            "B": "image/question/exam/XHTD_04_B.B.gif",
            "C": "image/question/exam/XHTD_04_B.C.gif",
            "D": "image/question/exam/XHTD_04_B.D.gif",
        }
    ]
    GDGT = [
        {
            "image_path": "image/question/exam/GDGT_01_C.gif",
            "correct_answer": "image/question/exam/GDGT_01_C.gif".split(".")[0][-1],
            "A": "image/question/exam/GDGT_01_C.A.gif",
            "B": "image/question/exam/GDGT_01_C.B.gif",
            "C": "image/question/exam/GDGT_01_C.C.gif",
            "D": "image/question/exam/GDGT_01_C.D.gif",
        },
        {
            "image_path": "image/question/exam/GDGT_02_B.gif",
            "correct_answer": "image/question/exam/GDGT_02_B.gif".split(".")[0][-1],
            "A": "image/question/exam/GDGT_02_B.A.gif",
            "B": "image/question/exam/GDGT_02_B.B.gif",
            "C": "image/question/exam/GDGT_02_B.C.gif",
            "D": "image/question/exam/GDGT_02_B.D.gif",
        },
        {
            "image_path": "image/question/exam/GDGT_03_C.gif",
            "correct_answer": "image/question/exam/GDGT_03_C.gif".split(".")[0][-1],
            "A": "image/question/exam/GDGT_03_C.A.gif",
            "B": "image/question/exam/GDGT_03_C.B.gif",
            "C": "image/question/exam/GDGT_03_C.C.gif",
            "D": "image/question/exam/GDGT_03_C.D.gif",
        },
        {
            "image_path": "image/question/exam/GDGT_04_A.gif",
            "correct_answer": "image/question/exam/GDGT_04_A.gif".split(".")[0][-1],
            "A": "image/question/exam/GDGT_04_A.A.gif",
            "B": "image/question/exam/GDGT_04_A.B.gif",
            "C": "image/question/exam/GDGT_04_A.C.gif",
            "D": "image/question/exam/GDGT_04_A.D.gif",
        }
    ]
    ATM = [
        {
            "image_path": "image/question/exam/ATM_01_B.gif",
            "correct_answer": "image/question/exam/ATM_01_B.gif".split(".")[0][-1],
            "A": "image/question/exam/ATM_01_B.A.gif",
            "B": "image/question/exam/ATM_01_B.B.gif",
            "C": "image/question/exam/ATM_01_B.C.gif",
            "D": "image/question/exam/ATM_01_B.D.gif",
        },
        {
            "image_path": "image/question/exam/ATM_02_C.gif",
            "correct_answer": "image/question/exam/ATM_02_C.gif".split(".")[0][-1],
            "A": "image/question/exam/ATM_02_C.A.gif",
            "B": "image/question/exam/ATM_02_C.B.gif",
            "C": "image/question/exam/ATM_02_C.C.gif",
            "D": "image/question/exam/ATM_02_C.D.gif",
        },
        {
            "image_path": "image/question/exam/ATM_03_D.gif",
            "correct_answer": "image/question/exam/ATM_03_D.gif".split(".")[0][-1],
            "A": "image/question/exam/ATM_03_D.A.gif",
            "B": "image/question/exam/ATM_03_D.B.gif",
            "C": "image/question/exam/ATM_03_D.C.gif",
            "D": "image/question/exam/ATM_03_D.D.gif",
        }
    ]
    TLDT = [
        {
            "image_path": "image/question/exam/TLĐT_01_B.gif",
            "correct_answer": "image/question/exam/TLĐT_01_B.gif".split(".")[0][-1],
            "A": "image/question/exam/TLĐT_01_B.A.gif",
            "B": "image/question/exam/TLĐT_01_B.B.gif",
            "C": "image/question/exam/TLĐT_01_B.C.gif",
            "D": "image/question/exam/TLĐT_01_B.D.gif",
        },
        {
            "image_path": "image/question/exam/TLĐT_02_A.gif",
            "correct_answer": "image/question/exam/TLĐT_02_A.gif".split(".")[0][-1],
            "A": "image/question/exam/TLĐT_02_A.A.gif",
            "B": "image/question/exam/TLĐT_02_A.B.gif",
            "C": "image/question/exam/TLĐT_02_A.C.gif",
            "D": "image/question/exam/TLĐT_02_A.D.gif",
        },
        {
            "image_path": "image/question/exam/TLĐT_03_B.gif",
            "correct_answer": "image/question/exam/TLĐT_03_B.gif".split(".")[0][-1],
            "A": "image/question/exam/TLĐT_03_B.A.gif",
            "B": "image/question/exam/TLĐT_03_B.B.gif",
            "C": "image/question/exam/TLĐT_03_B.C.gif",
            "D": "image/question/exam/TLĐT_03_B.D.gif",
        }
    ]


class GameSetting:
    selected_subject = None  # All & (Math or History or ...)
    selected_game = None  # Flappy_Bird or Apple_Catcher or Word_Search
    selected_level = None  # 1 or 2 or 3 or 4
    selected_game_mode = None  # Normal or Rank


class ExamSetting:
    selected_subject = Exam.ATGT


class ToolTip:
    learn_screen = "EverStudy\nĐây là hướng dẫn sử dụng của màn hình Ôn tập."
    game_screen = "EverStudy\nĐây là hướng dẫn sử dụng của màn hình Trò chơi.\nChọn trò chơi mà bạn muốn chơi."
    game_screen_mode = ("EverStudy\nĐây là hướng dẫn sử dụng của màn hình Trò chơi.\nChọn chế độ mà bạn muốn chơi."
                        "\nChơi thường sẽ không tính điểm xếp hạng."
                        "\nChơi xếp hạng để tham gia đua top cùng mọi người.")
    utility_screen = ("EverStudy\nĐây là hướng dẫn sử dụng của màn hình Tiện ích."
               "\nBạn có thể chọn sử dụng tiện ích mà bạn cần.")
    share_screen = ("EverStudy\nĐây là hướng dẫn sử dụng của màn hình Chia sẻ."
                    "\nBạn có thể chia sẻ mọi thứ cùng giáo viên."
                    "\nMọi thông tin sẽ được bí mật.")
    calculate_screen = ("EverStudy\nĐây là hướng dẫn sử dụng của màn hình Kết quả học tập."
                        "\nBạn có thể tính toán điểm Trung bình môn và Kết quả học tập của bản thân.")
    time_table_screen = ("EverStudy\nĐây là hướng dẫn sử dụng của màn hình Thời khóa biểu."
                         "\nBạn có thể lưu trữ thời khóa biểu thông qua hình ảnh, có 2 hình ảnh để bạn tùy chỉnh.")
    exam_screen = ("EverStudy\nĐây là hướng dẫn sử dụng của màn hình Thi."
                   "\nBạn có thể tham gia trả lời các câu hỏi theo từng bài thi có sẵn.")
    chat_gpt_screen = ("EverStudy\nĐây là hướng dẫn sử dụng của màn hình Chat cùng AI."
                      "\nBạn có thể hỏi đáp các thắc mắc cùng EverStudy AI tại đây."
                      "\nĐừng ngại hỏi nếu bạn không biết, cùng trau dồi kiến thức nào.")