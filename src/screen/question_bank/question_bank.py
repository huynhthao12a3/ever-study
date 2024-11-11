from tkinter import messagebox

from src.utils.component import Component
from src.utils.constant import ImageUrl, ToolTip, AppSetting
from src.utils.file import FileManager
from src.utils.gif import AnimatedGifCanvas
import tkinter as tk


class QuestionBankScreen(tk.Frame):
    def __init__(self, master, callback_list, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        self.master = master
        self.show_utility_screen = callback_list["UtilityScreen"]
        self.show_subject_screen = callback_list["SubjectScreen"]

    def load_widgets(self):
        gif_path = ImageUrl.bg_question_bank_screen
        animated_canvas = AnimatedGifCanvas(self, gif_path, self.on_click)
        animated_canvas.pack()

        # Handle change cursor
        animated_canvas.add_clickable_area(85, 120, 315, 200)  # 1. Toán
        animated_canvas.add_clickable_area(500, 120, 725, 200)  # 2. Ngữ Văn
        animated_canvas.add_clickable_area(35, 210, 265, 285)  # 3. Tiếng Anh
        animated_canvas.add_clickable_area(550, 210, 780, 285)  # 4. KHTN
        animated_canvas.add_clickable_area(35, 315, 265, 390)  # 5. LS&DL
        animated_canvas.add_clickable_area(550, 315, 780, 390)  # 6. Tin Học
        animated_canvas.add_clickable_area(85, 400, 315, 480)  # 7. GDCD
        animated_canvas.add_clickable_area(500, 400, 725, 480)  # 8. Công Nghệ

        Component.left_label(self)
        Component.right_button_back(self, self.show_utility_screen)
        Component.right_button_intro(self, ToolTip.question_bank_screen)

    def on_click(self, x, y):
        print(f"Clicked on Page at x={x}, y={y}")
        if 85 < x < 315 and 120 < y < 200:
            print("1. Toán")
            if AppSetting.selected_grade == "grade_9":
                messagebox.showinfo("Thông báo", "Năm học 2024-2025 học chương trình mới nên chưa có đề cương.\nVui lòng quay lại sau.")
            else:
                AppSetting.subject_instance = AppSetting.utility_instance.math
                self.show_subject_screen()
        if 500 < x < 725 and 120 < y < 200:
            print("2. Ngữ Văn")
            if AppSetting.selected_grade == "grade_9":
                messagebox.showinfo("Thông báo", "Năm học 2024-2025 học chương trình mới nên chưa có đề cương.\nVui lòng quay lại sau.")
            else:
                AppSetting.subject_instance = AppSetting.utility_instance.literature
                self.show_subject_screen()
        if 35 < x < 265 and 210 < y < 285:
            print("3. Tiếng Anh")
            if AppSetting.selected_grade == "grade_9":
                messagebox.showinfo("Thông báo", "Năm học 2024-2025 học chương trình mới nên chưa có đề cương.\nVui lòng quay lại sau.")
            else:
                AppSetting.subject_instance = AppSetting.utility_instance.english
                self.show_subject_screen()
        if 550 < x < 780 and 210 < y < 285:
            print("4. KHTN")
            if AppSetting.selected_grade == "grade_9":
                messagebox.showinfo("Thông báo", "Năm học 2024-2025 học chương trình mới nên chưa có đề cương.\nVui lòng quay lại sau.")
            else:
                AppSetting.subject_instance = AppSetting.utility_instance.natural_sciences
                self.show_subject_screen()
        if 35 < x < 265 and 315 < y < 390:
            print("5. LS&DL")
            if AppSetting.selected_grade == "grade_9":
                messagebox.showinfo("Thông báo", "Năm học 2024-2025 học chương trình mới nên chưa có đề cương.\nVui lòng quay lại sau.")
            else:
                AppSetting.subject_instance = AppSetting.utility_instance.history_geography
                self.show_subject_screen()
        if 550 < x < 780 and 315 < y < 390:
            print("6. Tin Học")
            if AppSetting.selected_grade == "grade_9":
                messagebox.showinfo("Thông báo", "Năm học 2024-2025 học chương trình mới nên chưa có đề cương.\nVui lòng quay lại sau.")
            else:
                AppSetting.subject_instance = AppSetting.utility_instance.computer_science
                self.show_subject_screen()
        if 85 < x < 315 and 400 < y < 480:
            print("7. GDCD")
            if AppSetting.selected_grade == "grade_9":
                messagebox.showinfo("Thông báo", "Năm học 2024-2025 học chương trình mới nên chưa có đề cương.\nVui lòng quay lại sau.")
            else:
                AppSetting.subject_instance = AppSetting.utility_instance.civic_education
                self.show_subject_screen()
        if 500 < x < 725 and 400 < y < 480:
            print("8. Công Nghệ")
            if AppSetting.selected_grade == "grade_9":
                messagebox.showinfo("Thông báo", "Năm học 2024-2025 học chương trình mới nên chưa có đề cương.\nVui lòng quay lại sau.")
            else:
                AppSetting.subject_instance = AppSetting.utility_instance.technology
                self.show_subject_screen()
