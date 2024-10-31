import tkinter as tk
from tkinter import messagebox

import requests

from src.utils.component import Component
from src.utils.constant import Auth, ImageUrl, Api
from src.utils.gif import AnimatedGifCanvas


class HomeScreen(tk.Frame):
    def __init__(self, master, callback_list, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        self.animated_canvas = None
        self.master = master
        self.show_learn_screen = callback_list["LearnScreen"]
        self.show_calculate_screen = callback_list["CalculateScreen"]
        self.show_game_screen = callback_list["GameScreen"]
        self.show_utility_screen = callback_list["UtilityScreen"]
        self.show_share_screen = callback_list["ShareScreen"]
        self.show_author_screen = callback_list["AuthorScreen"]
        self.show_login_screen = callback_list["LoginScreen"]

    def load_widgets(self):
        gif_path = ImageUrl.bg_home_screen
        self.animated_canvas = AnimatedGifCanvas(self, gif_path, self.on_click)
        self.animated_canvas.pack()

        # Handle change cursor
        self.animated_canvas.add_clickable_area(75, 150, 270, 310)  # Learn Screen
        self.animated_canvas.add_clickable_area(325, 120, 470, 310)  # Game Screen
        self.animated_canvas.add_clickable_area(526, 135, 720, 310)  # Utility Screen
        self.animated_canvas.add_clickable_area(335, 350, 465, 525)  # Share Screen
        self.animated_canvas.add_clickable_area(1, 520, 60, 600)     # Author Screen (left)
        self.animated_canvas.add_clickable_area(750, 490, 800, 600)  # Author Screen (right)

        Component.left_label(self)

        if Auth.login_success is False:
            Component.right_button_login(self, self.show_login_screen)

    def on_click(self, x, y):
        print(f"Clicked on Page at x={x}, y={y}")
        if Auth.login_success is True or Auth.login_success is False:
            if 75 < x < 270 and 150 < y < 310:
                print("Learn Screen")
                self.show_learn_screen()

            if 325 < x < 470 and 120 < y < 310:
                print("Game Screen")
                self.show_game_screen()

            if 526 < x < 720 and 135 < y < 310:
                print("Utility Screen")
                self.show_utility_screen()

            if 335 < x < 465 and 350 < y < 525:
                print("Share Screen")
                self.show_share_screen()

            if (1 < x < 60 and 520 < y < 600) or (750 < x < 800 and 490 < y < 600):
                print("Author Screen")
                self.show_author_screen()
        else:
            messagebox.showinfo("Thông báo", "Vui lòng đăng nhập để sử dụng ứng dụng.")
