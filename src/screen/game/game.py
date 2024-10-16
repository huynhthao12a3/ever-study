from src.utils.component import Component
from src.utils.constant import ImageUrl, Api, Auth, Font, GameSetting, ToolTip
from src.utils.gif import AnimatedGifCanvas
import tkinter as tk


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
        Component.right_button_intro(self, ToolTip.game_screen)

    def on_click(self, x, y):
        print(f"Clicked on Page at x={x}, y={y}")
        if 70 < x < 245 and 220 < y < 430:
            GameSetting.selected_game = "Flappy_Bird"
            self.show_game_mode_screen()
        if 335 < x < 520 and 220 < y < 430:
            GameSetting.selected_game = "Apple_Catcher"
            self.show_game_mode_screen()
        if 590 < x < 750 and 220 < y < 430:
            GameSetting.selected_game = "Word_Search"
            self.show_game_mode_screen()
