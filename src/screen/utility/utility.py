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
        self.show_exam_screen = callback_list["ExamScreen"]
        self.show_chat_ai_screen = callback_list["ChatAIScreen"]

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
            self.show_calculate_screen()
        if 335 < x < 485 and 135 < y < 325:
            self.show_time_table_screen()
        if 575 < x < 730 and 135 < y < 325:
            messagebox.showinfo("Thông báo", f"Tính năng này đang phát trển.\nVui lòng quay lại sau.")
        if 95 < x < 245 and 365 < y < 535:
            self.show_exam_screen()
        if 575 < x < 730 and 365 < y < 535:
            self.show_chat_ai_screen()
