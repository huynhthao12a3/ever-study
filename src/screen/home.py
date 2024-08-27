import pygame
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import font as tkfont
from src.screen.author import AuthorScreen
from src.screen.calculate import CalculateScreen
from src.screen.game import GameScreen
from src.screen.learn import LearnScreen
from src.screen.other import OtherScreen
from src.utils.constant import InfoRect, Auth
from src.utils.file import FileManager
from src.utils.gif import AnimatedGifCanvas
from src.utils.popup import ErasablePopup


class HomeScreen(tk.Frame):
    def __init__(self, master, callback_list, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        self.animated_canvas = None
        self.master = master
        self.show_learn_screen = callback_list["LearnScreen"]
        self.show_calculate_screen = callback_list["CalculateScreen"]
        self.show_game_screen = callback_list["GameScreen"]
        self.show_discovery_screen = callback_list["DiscoveryScreen"]
        self.show_share_screen = callback_list["ShareScreen"]
        self.show_other_screen = callback_list["OtherScreen"]
        self.show_author_screen = callback_list["AuthorScreen"]
        self.show_login_screen = callback_list["LoginScreen"]

        # self.load_widgets()

    def load_widgets(self):
        gif_path = "image/background/home.gif"
        self.animated_canvas = AnimatedGifCanvas(self, gif_path, self.on_click)
        self.animated_canvas.pack()

        label = tk.Label(self, text="Hi, " + Auth.full_name if Auth.login_success else "", font=("Roboto", 12),
                         bg="white", borderwidth=2)
        label.place(x=0, y=2)
        label.bind("<Button-1>", lambda e: self.mouse_click())

        button = tk.Button(self, text="Đăng nhập", command=self.show_login_screen)
        button.place(x=728, y=4)

    def on_click(self, x, y):
        print(f"Clicked on Page at x={x}, y={y}")
        if 50 < x < 270 and 155 < y < 260:
            print("Learn Screen")
            self.show_learn_screen()
        if 300 < x < 520 and 155 < y < 260:
            print("Calculate Screen")
            self.show_calculate_screen()
        if 555 < x < 777 and 155 < y < 260:
            print("Game Screen")
            self.show_game_screen()
        if 50 < x < 270 and 350 < y < 455:
            print("Discovery Screen")
            self.show_discovery_screen()
        if 300 < x < 520 and 350 < y < 455:
            print("Share Screen")
            self.show_share_screen()
        if 555 < x < 777 and 350 < y < 455:
            print("Other Screen")
            self.show_other_screen()

        if 370 < x < 640 and 550 < y < 599:
            print("Author Screen")
            self.show_author_screen()

    def mouse_click(self):
        print("mouse click")
