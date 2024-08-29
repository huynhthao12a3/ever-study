from src.utils.component import Component
from src.utils.constant import ImageUrl
from src.utils.file import FileManager
from src.utils.gif import AnimatedGifCanvas
from src.screen.game.flappybird.main import FlappyBird
import tkinter as tk


class GameScreen(tk.Frame):
    def __init__(self, master, callback_list, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        self.master = master
        self.show_home_screen = callback_list["HomeScreen"]

    def load_widgets(self):
        gif_path = ImageUrl.bg_game_screen
        animated_canvas = AnimatedGifCanvas(self, gif_path, self.on_click)
        animated_canvas.pack()

        Component.left_label(self)
        Component.right_button_back(self, self.show_home_screen)

        flappy_bird = tk.Button(self, text="Flappy Bird", font=("Roboto", 20, "bold"), command=self.show_fappy_bird_game)
        flappy_bird.place(x=50, y=50)

    def on_click(self, x, y):
        print(f"Clicked on Page at x={x}, y={y}")

    def show_fappy_bird_game(self):
        FlappyBird().run()
