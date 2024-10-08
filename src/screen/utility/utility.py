from tkinter import messagebox

from src.utils.component import Component
from src.utils.constant import ImageUrl
from src.utils.file import FileManager
from src.utils.gif import AnimatedGifCanvas
import tkinter as tk


class UtilityScreen(tk.Frame):
    def __init__(self, master, callback_list, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        self.master = master
        self.show_home_screen = callback_list["HomeScreen"]
        self.show_calculate_screen = callback_list["CalculateScreen"]
        self.show_time_table_screen = callback_list["TimeTableScreen"]

        # self.load_widgets()

    def load_widgets(self):
        gif_path = ImageUrl.bg_utility_screen
        animated_canvas = AnimatedGifCanvas(self, gif_path, self.on_click)
        animated_canvas.pack()

        Component.left_label(self)
        Component.right_button_back(self, self.show_home_screen)

    def on_click(self, x, y):
        print(f"Clicked on Page at x={x}, y={y}")
        if 95 < x < 245 and 135 < y < 325:
            print("ket qua hoc tap")
            self.show_calculate_screen()
        if 335 < x < 485 and 135 < y < 325:
            print("tkb")
            self.show_time_table_screen()
        if 575 < x < 730 and 135 < y < 325:
            print("kho de")
            messagebox.showinfo("Chưa có ý tưởng", f"Từ từ làm sau, ghi chú tạm đây")
        if 95 < x < 245 and 365 < y < 535:
            print("thi")
            messagebox.showinfo("Chưa có ý tưởng", f"Từ từ làm sau, ghi chú tạm đây")
        if 575 < x < 730 and 365 < y < 535:
            print("ai")
            messagebox.showinfo("Chưa có ý tưởng", f"Từ từ làm sau, ghi chú tạm đây")
