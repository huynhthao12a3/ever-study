import tkinter as tk
from PIL import Image, ImageTk

from src.utils.file import FileManager


class AnimatedGifCanvas(tk.Canvas):
    def __init__(self, master, filename, on_click_callback, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        self.sequence = []
        self.delay = 100

        self.load_gif(filename)
        self.on_click_callback = on_click_callback
        self.bind("<Button-1>", self.on_click)

    def load_gif(self, filename):
        self.gif = Image.open(FileManager().resource_path(filename))
        self.gif.load()
        self.gif_width, self.gif_height = self.gif.size

        try:
            while True:
                self.sequence.append(self.gif.copy())
                self.gif.seek(self.gif.tell() + 1)
        except EOFError:
            pass

        self.show_frame(0)

    def show_frame(self, frame_num):
        if self.sequence:
            self.current_frame = frame_num % len(self.sequence)
            self.gif_frame = ImageTk.PhotoImage(self.sequence[self.current_frame])

            self.configure(width=self.gif_width, height=self.gif_height)
            self.create_image(0, 0, anchor=tk.NW, image=self.gif_frame)

            self.after(self.delay, lambda: self.show_frame(self.current_frame + 1))
        else:
            pass

    def on_click(self, event):
        x = event.x
        y = event.y
        self.on_click_callback(x, y)
