from tkinter import messagebox

from src.screen.game.applecatcher.main import AppleCatcher
from src.utils.component import Component
from src.utils.constant import ImageUrl, Api, Auth, Font, GameSetting
from src.utils.file import FileManager
from src.utils.gif import AnimatedGifCanvas
from src.screen.game.flappybird.main import FlappyBird
from src.screen.game.animalwordsearch.main import AnimalWordSearch
import tkinter as tk
# Call api, convert json library
import requests
import json


class GameScreen(tk.Frame):
    def __init__(self, master, callback_list, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        self.root = self.winfo_toplevel()  # Get parent window (Tk)
        self.master = master
        self.show_home_screen = callback_list["HomeScreen"]
        self.show_game_mode_screen = callback_list["GameModeScreen"]
        self.pygame_window_closed = False

    def load_widgets(self):
        gif_path = ImageUrl.bg_game_screen
        animated_canvas = AnimatedGifCanvas(self, gif_path, self.on_click)
        animated_canvas.pack()

        Component.left_label(self)
        Component.right_button_back(self, self.show_home_screen)

    def on_click(self, x, y):
        print(f"Clicked on Page at x={x}, y={y}")
        if 70 < x < 245 and 220 < y < 430:
            print("Flappy Bird")
            GameSetting.selected_game = "Flappy_Bird"
            self.show_game_mode_screen()
        if 335 < x < 520 and 220 < y < 430:
            print("Apple Collection")
            GameSetting.selected_game = "Apple_Catcher"
            self.show_game_mode_screen()
        if 590 < x < 750 and 220 < y < 430:
            print("Word Search")
            GameSetting.selected_game = "Word_Search"
            messagebox.showinfo("Đang làm", f"Game này đang chỉnh sửa, chưa hoàn thiện.")
            # self.show_game_mode_screen()
