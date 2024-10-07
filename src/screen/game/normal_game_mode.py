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

        self.root = self.winfo_toplevel()  # Get parent window (Tk)
        self.master = master
        self.show_home_screen = callback_list["HomeScreen"]
        self.show_game_screen = callback_list["GameScreen"]
        self.pygame_window_closed = False

    def load_widgets(self):
        gif_path = ImageUrl.bg_normal_game_mode_screen
        animated_canvas = AnimatedGifCanvas(self, gif_path, self.on_click)
        animated_canvas.pack()

        Component.left_label(self)
        Component.right_button_back(self, self.show_game_screen)

    def on_click(self, x, y):
        print(f"Clicked on Page at x={x}, y={y}")
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
            if GameSetting.selected_game == "Word_Search":
                self.animal_word_search_run(GameSetting.selected_subject)

    def flappy_bird_run(self, game_mode):
        self.root.withdraw()  # Hide Tkinter window
        FlappyBird(self.on_flappy_bird_close, game_mode).run()

    def apple_catcher_run(self, game_mode):
        self.root.withdraw()  # Hide Tkinter window
        AppleCatcher(self.on_apple_catcher_close, game_mode).run()

    def animal_word_search_run(self, game_mode):
        self.root.withdraw()  # Hide Tkinter window
        AnimalWordSearch(self.on_animal_word_search_close, game_mode).run()

    def on_flappy_bird_close(self, game_result=None):
        self.root.deiconify()  # Show Tkinter window
        print("flappy bird closed - normal game mode")

    def on_apple_catcher_close(self, game_result=None):
        self.root.deiconify()  # Show Tkinter window
        print("Apple Catcher closed - normal game mode")

    def on_animal_word_search_close(self, game_result=None):
        self.root.deiconify()  # Show Tkinter window
        print("Animal Word Search closed - normal game mode")