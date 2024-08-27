from src.utils.file import FileManager
from src.utils.gif import AnimatedGifCanvas
import tkinter as tk


class DiscoveryScreen(tk.Frame):
    def __init__(self, master, callback_list, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        self.master = master
        self.show_home_screen = callback_list["HomeScreen"]

        # self.load_widgets()

    def load_widgets(self):
        gif_path = "image/background/hoc-tap.gif"
        animated_canvas = AnimatedGifCanvas(self, gif_path, self.on_click)
        animated_canvas.pack()

        label = tk.Label(self, text="Page 2", font=("Arial", 16), bg="white")
        label.place(relx=0.5, rely=0.1, anchor=tk.CENTER)

        button = tk.Button(self, text="Go to Page 1", command=self.show_home_screen)
        button.place(relx=0.5, rely=0.9, anchor=tk.CENTER)

    def on_click(self, x, y):
        print(f"Clicked on Page at x={x}, y={y}")
