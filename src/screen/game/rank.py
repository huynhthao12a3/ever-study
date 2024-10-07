from src.utils.component import Component
from src.utils.constant import ImageUrl
from src.utils.gif import AnimatedGifCanvas
import tkinter as tk


class RankScreen(tk.Frame):
    def __init__(self, master, callback_list, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        self.root = self.winfo_toplevel()  # Get parent window (Tk)
        self.master = master
        self.show_home_screen = callback_list["HomeScreen"]
        self.show_game_mode_screen = callback_list["GameModeScreen"]

    def load_widgets(self):
        gif_path = ImageUrl.bg_rank_screen
        animated_canvas = AnimatedGifCanvas(self, gif_path, self.on_click)
        animated_canvas.pack()

        Component.left_label(self)
        Component.right_button_back(self, self.show_game_mode_screen)

    def on_click(self, x, y):
        print(f"Clicked on Page at x={x}, y={y}")
