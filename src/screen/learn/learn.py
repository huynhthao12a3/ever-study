from src.utils.component import Component
from src.utils.constant import Auth, ImageUrl
from src.utils.file import FileManager
from src.utils.gif import AnimatedGifCanvas
import tkinter as tk


class LearnScreen(tk.Frame):
    def __init__(self, master, callback_list, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        self.master = master
        self.show_home_screen = callback_list["HomeScreen"]

        # self.load_widgets()

    def load_widgets(self):
        gif_path = ImageUrl.bg_learn_screen
        animated_canvas = AnimatedGifCanvas(self, gif_path, self.on_click)
        animated_canvas.pack()

        Component.left_label(self)
        Component.right_button_back(self, self.show_home_screen)

    def on_click(self, x, y):
        print(f"Clicked on Page at x={x}, y={y}")
