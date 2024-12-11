import webbrowser
from tkinter import messagebox

from src.utils.component import Component
from src.utils.constant import Auth, ImageUrl, ToolTip, AppSetting
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
        self.show_learn_subject_screen = callback_list["LearnSubjectScreen"]
        self.file_manager = FileManager()

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
            # self.show_math_screen()
            # webbrowser.open(self.file_manager.resource_path("file/on-tap/" + AppSetting.learn_instance.f_toan))
            AppSetting.subject_instance = AppSetting.learn_instance.math
            self.show_learn_subject_screen()

        if 110 < x < 310 and 200 < y < 300:
            print("Môn Tiếng anh")
            # webbrowser.open(self.file_manager.resource_path("file/on-tap/" + AppSetting.learn_instance.f_tienganh))
            # messagebox.showinfo("Thông báo", "Ứng dụng đang trong quá trình chuẩn bị tài liệu.\nVui lòng quay lại sau.")
            AppSetting.subject_instance = AppSetting.learn_instance.english
            self.show_learn_subject_screen()

        if 110 < x < 310 and 330 < y < 430:
            print("Môn LS-DL")
            # webbrowser.open(self.file_manager.resource_path("file/on-tap/" + AppSetting.learn_instance.f_lsdl))
            # messagebox.showinfo("Thông báo", "Ứng dụng đang trong quá trình chuẩn bị tài liệu.\nVui lòng quay lại sau.")
            AppSetting.subject_instance = AppSetting.learn_instance.history_geography
            self.show_learn_subject_screen()

        if 110 < x < 310 and 450 < y < 550:
            print("Môn Tin học")
            # webbrowser.open(self.file_manager.resource_path("file/on-tap/" + AppSetting.learn_instance.f_tinhoc))
            # messagebox.showinfo("Thông báo", "Ứng dụng đang trong quá trình chuẩn bị tài liệu.\nVui lòng quay lại sau.")
            AppSetting.subject_instance = AppSetting.learn_instance.computer_science
            self.show_learn_subject_screen()

        if 475 < x < 685 and 80 < y < 180:
            print("Môn Ngữ văn")
            # webbrowser.open(self.file_manager.resource_path("file/on-tap/" + AppSetting.learn_instance.f_nguvan))
            # messagebox.showinfo("Thông báo", "Ứng dụng đang trong quá trình chuẩn bị tài liệu.\nVui lòng quay lại sau.")
            AppSetting.subject_instance = AppSetting.learn_instance.literature
            self.show_learn_subject_screen()

        if 475 < x < 685 and 200 < y < 300:
            print("Môn KHTN")
            # webbrowser.open(self.file_manager.resource_path("file/on-tap/" + AppSetting.learn_instance.f_khtn))
            # messagebox.showinfo("Thông báo", "Ứng dụng đang trong quá trình chuẩn bị tài liệu.\nVui lòng quay lại sau.")
            AppSetting.subject_instance = AppSetting.learn_instance.natural_sciences
            self.show_learn_subject_screen()

        if 475 < x < 685 and 330 < y < 430:
            print("Môn GDCD")
            # webbrowser.open(self.file_manager.resource_path("file/on-tap/" + AppSetting.learn_instance.f_gdcd))
            # messagebox.showinfo("Thông báo", "Ứng dụng đang trong quá trình chuẩn bị tài liệu.\nVui lòng quay lại sau.")
            AppSetting.subject_instance = AppSetting.learn_instance.civic_education
            self.show_learn_subject_screen()

        if 475 < x < 685 and 450 < y < 550:
            print("Môn Công nghệ")
            # webbrowser.open(self.file_manager.resource_path("file/on-tap/" + AppSetting.learn_instance.f_toan))
            messagebox.showinfo("Thông báo", "Ứng dụng đang trong quá trình chuẩn bị tài liệu.\nVui lòng quay lại sau.")
            # AppSetting.subject_instance = AppSetting.learn_instance.math
            # self.show_learn_subject_screen()
