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
        self.show_author_screen = callback_list["AuthorScreen"]
        self.show_game_screen = callback_list["GameScreen"]

        # self.load_widgets()

    def load_widgets(self):
        gif_path = "image/background/home.gif"
        self.animated_canvas = AnimatedGifCanvas(self, gif_path, self.on_click)
        self.animated_canvas.pack()

        label = tk.Label(self, text="Page 1", font=("Roboto", 12), bg="white", borderwidth=2)
        label.place(x=0, y=0)
        label.bind("<Button-1>", lambda e: self.test())

        button = tk.Button(self, text="Go to Page 2", command=self.show_game_screen)
        button.place(relx=0.5, rely=0.9, anchor=tk.CENTER)

    def on_click(self, x, y):
        print(f"Clicked on Page at x={x}, y={y}")
        if 50 < x < 270 and 155 < y < 260:
            print("Learn Screen")
            #     self.show_learn_screen()
        if 300 < x < 520 and 155 < y < 260:
            print("Calculate Screen")
        if 555 < x < 777 and 155 < y < 260:
            print("Game Screen")
        if 50 < x < 270 and 350 < y < 455:
            print("Discovery Screen")
            #     self.show_learn_screen()
        if 300 < x < 520 and 350 < y < 455:
            print("Share Screen")
        if 555 < x < 777 and 350 < y < 455:
            print("Other Screen")

        if 370 < x < 640 and 550 < y < 599:
            print("Author Screen")

    def test(self):
        print("click chuột")



