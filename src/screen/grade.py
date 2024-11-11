import tkinter as tk
from tkinter import messagebox

import requests

from src.utils.component import Component
from src.utils.constant import Auth, ImageUrl, Api, ToolTip, AppSetting, LearnFile06, BankFileUrl06, LearnFile07, \
    BankFileUrl07, LearnFile08, BankFileUrl08, LearnFile09, BankFileUrl09, Question06, Question07, Question08, \
    Question09
from src.utils.gif import AnimatedGifCanvas


class GradeScreen(tk.Frame):
    def __init__(self, master, callback_list, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        self.animated_canvas = None
        self.master = master
        self.show_home_screen = callback_list["HomeScreen"]
        self.show_learn_screen = callback_list["LearnScreen"]
        self.show_calculate_screen = callback_list["CalculateScreen"]
        self.show_game_screen = callback_list["GameScreen"]
        self.show_utility_screen = callback_list["UtilityScreen"]
        self.show_share_screen = callback_list["ShareScreen"]
        self.show_author_screen = callback_list["AuthorScreen"]
        self.show_login_screen = callback_list["LoginScreen"]

    def load_widgets(self):
        gif_path = ImageUrl.bg_grade_screen
        self.animated_canvas = AnimatedGifCanvas(self, gif_path, self.on_click)
        self.animated_canvas.pack()

        # Handle change cursor
        self.animated_canvas.add_clickable_area(140, 130, 355, 290)  # grade_6
        self.animated_canvas.add_clickable_area(460, 130, 670, 290)  # grade_7
        self.animated_canvas.add_clickable_area(140, 350, 355, 510)  # grade_8
        self.animated_canvas.add_clickable_area(460, 350, 670, 510)  # grade_9

        Component.left_label(self)
        Component.right_button_back(self, self.show_home_screen)
        Component.right_button_intro(self, ToolTip.grade_screen)

    def on_click(self, x, y):
        print(f"Clicked on Page at x={x}, y={y}")
        if 140 < x < 355 and 130 < y < 290:
            AppSetting.selected_grade = "grade_6"
            AppSetting.learn_instance = LearnFile06
            AppSetting.game_instance = Question06
            AppSetting.utility_instance = BankFileUrl06
        if 460 < x < 670 and 130 < y < 290:
            AppSetting.selected_grade = "grade_7"
            AppSetting.learn_instance = LearnFile07
            AppSetting.game_instance = Question07
            AppSetting.utility_instance = BankFileUrl07
        if 140 < x < 355 and 350 < y < 510:
            AppSetting.selected_grade = "grade_8"
            AppSetting.learn_instance = LearnFile08
            AppSetting.game_instance = Question08
            AppSetting.utility_instance = BankFileUrl08
        if 460 < x < 670 and 350 < y < 510:
            AppSetting.selected_grade = "grade_9"
            AppSetting.learn_instance = LearnFile09
            AppSetting.game_instance = Question09
            AppSetting.utility_instance = BankFileUrl09

        if AppSetting.selected_feature == "learn":
            self.show_learn_screen()
        elif AppSetting.selected_feature == "game":
            self.show_game_screen()
        elif AppSetting.selected_feature == "utility":
            self.show_utility_screen()
