from src.screen.game.applecatcher.main import AppleCatcher
from src.utils.component import Component
from src.utils.constant import ImageUrl, Api, Auth, Font, GameSetting
from src.utils.file import FileManager
from src.utils.gif import AnimatedGifCanvas
from src.screen.game.flappybird.main import FlappyBird
from src.screen.game.animalwordsearch.main import AnimalWordSearch
import tkinter as tk


class NormalGameModeScreen(tk.Frame):
    def __init__(self, master, callback_list, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        self.animated_canvas = None
        self.root = self.winfo_toplevel()  # Get parent window (Tk)
        self.master = master
        self.show_home_screen = callback_list["HomeScreen"]
        self.show_game_screen = callback_list["GameScreen"]
        self.show_game_mode_screen = callback_list["GameModeScreen"]
        self.show_word_search_mode_screen = callback_list["WordSearchModeScreen"]
        self.pygame_window_closed = False
        self.gif_path = None

    def load_widgets(self):
        if GameSetting.selected_game == "Flappy_Bird" or GameSetting.selected_game == "Apple_Catcher":
            self.gif_path = ImageUrl.bg_normal_game_mode_screen
        else:
            self.gif_path = ImageUrl.bg_word_search_mode_screen

        self.animated_canvas = AnimatedGifCanvas(self, self.gif_path, self.on_click)
        self.animated_canvas.pack()

        # Đăng ký các vùng có thể click
        if GameSetting.selected_game in ["Flappy_Bird", "Apple_Catcher"]:
            self.register_normal_game_clickable_areas()
        else:
            self.register_word_search_clickable_areas()

        Component.left_label(self)
        Component.right_button_back(self, self.show_game_mode_screen)

    def register_normal_game_clickable_areas(self):
        areas = [
            (110, 80, 310, 180),   # Môn Toán
            (110, 200, 310, 300),  # Môn Tiếng anh
            (110, 330, 310, 430),  # Môn LS-DL
            (110, 450, 310, 550),  # Môn Tin học
            (475, 80, 685, 180),   # Môn Ngữ văn
            (475, 200, 685, 300),  # Môn KHTN
            (475, 330, 685, 430),  # Môn GDCD
            (475, 450, 685, 550),  # Môn Công nghệ
        ]
        for area in areas:
            self.animated_canvas.add_clickable_area(*area)

    def register_word_search_clickable_areas(self):
        areas = [
            (55, 270, 135, 350),   # Toán - 1
            (165, 270, 245, 350),  # Toán - 2
            (55, 370, 135, 450),   # Toán - 3
            (165, 370, 245, 450),  # Toán - 4
            (305, 270, 385, 350),  # Tiếng Anh - 1
            (415, 270, 495, 350),  # Tiếng Anh - 2
            (305, 370, 385, 450),  # Tiếng Anh - 3
            (415, 370, 495, 450),  # Tiếng Anh - 4
            (555, 270, 635, 350),  # LS-DL - 1
            (665, 270, 745, 350),  # LS-DL - 2
            (555, 370, 635, 450),  # LS-DL - 3
            (665, 370, 745, 450),  # LS-DL - 4
        ]
        for area in areas:
            self.animated_canvas.add_clickable_area(*area)

    def on_click(self, x, y):
        print(f"Clicked on Page at x={x}, y={y}")
        if GameSetting.selected_game == "Flappy_Bird" or GameSetting.selected_game == "Apple_Catcher":
            if 110 < x < 310 and 80 < y < 180:
                print("Môn Toán")
                GameSetting.selected_subject = "math"
            if 110 < x < 310 and 200 < y < 300:
                print("Môn Tiếng anh")
                GameSetting.selected_subject = "english"
            if 110 < x < 310 and 330 < y < 430:
                print("Môn LS-DL")
                GameSetting.selected_subject = "history_geography"
            if 110 < x < 310 and 450 < y < 550:
                print("Môn Tin học")
                GameSetting.selected_subject = "computer_science"

            if 475 < x < 685 and 80 < y < 180:
                print("Môn Ngữ văn")
                GameSetting.selected_subject = "literature"
            if 475 < x < 685 and 200 < y < 300:
                print("Môn KHTN")
                GameSetting.selected_subject = "natural_sciences"
            if 475 < x < 685 and 330 < y < 430:
                print("Môn GDCD")
                GameSetting.selected_subject = "civic_education"
            if 475 < x < 685 and 450 < y < 550:
                print("Môn Công nghệ")
                GameSetting.selected_subject = "technology"

            if GameSetting.selected_subject is not None:
                if GameSetting.selected_game == "Flappy_Bird":
                    self.flappy_bird_run(GameSetting.selected_subject)
                if GameSetting.selected_game == "Apple_Catcher":
                    self.apple_catcher_run(GameSetting.selected_subject)
        else:
            print("animal_word_search_run")
            if 55 < x < 135 and 270 < y < 350:
                print("Toán - 1")
                self.animal_word_search_run("math", "lv1")
            if 165 < x < 245 and 270 < y < 350:
                print("Toán - 2")
                self.animal_word_search_run("math", "lv2")
            if 55 < x < 135 and 370 < y < 450:
                print("Toán - 3")
                self.animal_word_search_run("math", "lv3")
            if 165 < x < 245 and 370 < y < 450:
                print("Toán - 4")
                self.animal_word_search_run("math", "lv4")

            if 305 < x < 385 and 270 < y < 350:
                print("Tiếng Anh - 1")
                self.animal_word_search_run("english", "lv1")
            if 415 < x < 495 and 270 < y < 350:
                print("Tiếng Anh - 2")
                self.animal_word_search_run("english", "lv2")
            if 305 < x < 385 and 370 < y < 450:
                print("Tiếng Anh - 3")
                self.animal_word_search_run("english", "lv3")
            if 415 < x < 495 and 370 < y < 450:
                print("Tiếng Anh - 4")
                self.animal_word_search_run("english", "lv4")

            if 555 < x < 635 and 270 < y < 350:
                print("LS-DL - 1")
                self.animal_word_search_run("history", "lv1")
            if 665 < x < 745 and 270 < y < 350:
                print("LS-DL - 2")
                self.animal_word_search_run("history", "lv2")
            if 555 < x < 635 and 370 < y < 450:
                print("LS-DL - 3")
                self.animal_word_search_run("history", "lv3")
            if 665 < x < 745 and 370 < y < 450:
                print("LS-DL - 4")
                self.animal_word_search_run("history", "lv4")

    def flappy_bird_run(self, selected_subject):
        self.root.withdraw()  # Hide Tkinter window
        FlappyBird(self.on_flappy_bird_close, selected_subject).run()

    def apple_catcher_run(self, selected_subject):
        self.root.withdraw()  # Hide Tkinter window
        AppleCatcher(self.on_apple_catcher_close, selected_subject).run()

    def animal_word_search_run(self, selected_subject, selected_level):
        self.root.withdraw()  # Hide Tkinter window
        AnimalWordSearch(self.on_animal_word_search_close, selected_subject, selected_level).run()

    def on_flappy_bird_close(self, game_result=None):
        self.root.deiconify()  # Show Tkinter window

    def on_apple_catcher_close(self, game_result=None):
        self.root.deiconify()  # Show Tkinter window

    def on_animal_word_search_close(self, game_result=None):
        self.root.deiconify()  # Show Tkinter window
