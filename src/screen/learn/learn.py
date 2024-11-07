from tkinter import messagebox

from src.utils.component import Component
from src.utils.constant import Auth, ImageUrl, ToolTip
from src.utils.file import FileManager
from src.utils.gif import AnimatedGifCanvas
import tkinter as tk


class LearnScreen(tk.Frame):
    def __init__(self, master, callback_list, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        self.master = master
        self.show_home_screen = callback_list["HomeScreen"]
        self.show_grade_screen = callback_list["GradeScreen"]
        self.show_math_screen = callback_list["MathScreen"]

    def load_widgets(self):
        gif_path = ImageUrl.bg_learn_screen
        animated_canvas = AnimatedGifCanvas(self, gif_path, self.on_click)
        animated_canvas.pack()

        # Handle change cursor
        animated_canvas.add_clickable_area(110, 80, 310, 180)  # Toán
        animated_canvas.add_clickable_area(110, 200, 310, 300)  # Tiếng Anh
        animated_canvas.add_clickable_area(110, 330, 310, 430)  # LS-DL
        animated_canvas.add_clickable_area(110, 450, 310, 550)  # Tin Học
        animated_canvas.add_clickable_area(475, 80, 685, 180)  # Ngữ Văn
        animated_canvas.add_clickable_area(475, 200, 685, 300)  # KHTN
        animated_canvas.add_clickable_area(475, 330, 685, 430)  # GDCD
        animated_canvas.add_clickable_area(475, 450, 685, 550)  # Công Nghệ

        Component.left_label(self)
        Component.right_button_back(self, self.show_grade_screen)
        Component.right_button_intro(self, ToolTip.learn_screen)

    def on_click(self, x, y):
        print(f"Clicked on Page at x={x}, y={y}")

        if 110 < x < 310 and 80 < y < 180:
            print("Môn Toán")
            self.show_math_screen()
        if 110 < x < 310 and 200 < y < 300:
            print("Môn Tiếng anh")
            messagebox.showinfo("Thông báo", "Ứng dụng đang trong quá trình chuẩn bị tài liệu.\nVui lòng quay lại sau.")
        if 110 < x < 310 and 330 < y < 430:
            print("Môn LS-DL")
            messagebox.showinfo("Thông báo", "Ứng dụng đang trong quá trình chuẩn bị tài liệu.\nVui lòng quay lại sau.")
        if 110 < x < 310 and 450 < y < 550:
            print("Môn Tin học")
            messagebox.showinfo("Thông báo", "Ứng dụng đang trong quá trình chuẩn bị tài liệu.\nVui lòng quay lại sau.")

        if 475 < x < 685 and 80 < y < 180:
            print("Môn Ngữ văn")
            messagebox.showinfo("Thông báo", "Ứng dụng đang trong quá trình chuẩn bị tài liệu.\nVui lòng quay lại sau.")
        if 475 < x < 685 and 200 < y < 300:
            print("Môn KHTN")
            messagebox.showinfo("Thông báo", "Ứng dụng đang trong quá trình chuẩn bị tài liệu.\nVui lòng quay lại sau.")
        if 475 < x < 685 and 330 < y < 430:
            print("Môn GDCD")
            messagebox.showinfo("Thông báo", "Ứng dụng đang trong quá trình chuẩn bị tài liệu.\nVui lòng quay lại sau.")
        if 475 < x < 685 and 450 < y < 550:
            print("Môn Công nghệ")
            messagebox.showinfo("Thông báo", "Ứng dụng đang trong quá trình chuẩn bị tài liệu.\nVui lòng quay lại sau.")
