import tkinter as tk
from PIL import Image, ImageTk

from src.utils.file import FileManager


class AnimatedGifCanvas(tk.Canvas):
    def __init__(self, master, filename, on_click_callback=None, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        self.sequence = []
        self.delay = 100
        self.clickable_areas = []

        self.load_gif(filename)
        self.on_click_callback = on_click_callback
        self.bind("<Button-1>", self.on_click)
        self.bind("<Motion>", self.on_mouse_move)
        self.bind("<Leave>", self.on_mouse_leave)

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
        if self.on_click_callback:
            self.on_click_callback(x, y)

    def add_clickable_area(self, x1, y1, x2, y2, cursor="hand2"):
        self.clickable_areas.append((x1, y1, x2, y2, cursor))

    def is_in_clickable_area(self, x, y):
        for area in self.clickable_areas:
            x1, y1, x2, y2, cursor = area
            if x1 <= x <= x2 and y1 <= y <= y2:
                return cursor
        return None

    def on_mouse_move(self, event):
        cursor = self.is_in_clickable_area(event.x, event.y)
        if cursor:
            self.config(cursor=cursor)
        else:
            self.config(cursor="")

    def on_mouse_leave(self, event):
        self.config(cursor="")

    def clear_clickable_areas(self):
        self.clickable_areas.clear()