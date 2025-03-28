from src.utils.component import Component
from src.utils.constant import ImageUrl, ExamSetting, Exam, ToolTip
from src.utils.file import FileManager
from src.utils.gif import AnimatedGifCanvas
import tkinter as tk


class ExamScreen(tk.Frame):
    def __init__(self, master, callback_list, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        self.master = master
        self.show_utility_screen = callback_list["UtilityScreen"]
        self.show_exams_screen = callback_list["ExamsScreen"]

    def load_widgets(self):
        gif_path = ImageUrl.bg_exam_screen
        animated_canvas = AnimatedGifCanvas(self, gif_path, self.on_click)
        animated_canvas.pack()

        # Handle change cursor
        animated_canvas.add_clickable_area(95, 130, 225, 305)  # ATGT
        animated_canvas.add_clickable_area(340, 130, 460, 305)  # BLHD
        animated_canvas.add_clickable_area(610, 130, 730, 305)  # XHTD
        animated_canvas.add_clickable_area(95, 340, 225, 520)  # GDGT
        animated_canvas.add_clickable_area(340, 340, 460, 520)  # ATM
        animated_canvas.add_clickable_area(610, 340, 730, 520)  # TLDT

        # Component.left_label(self)
        Component.right_button_back(self, self.show_utility_screen)
        Component.right_button_intro(self, ToolTip.exam_screen)

    def on_click(self, x, y):
        print(f"Clicked on Page at x={x}, y={y}")
        if 95 < x < 225 and 130 < y < 305:
            print("ATGT")
            ExamSetting.selected_subject = Exam.ATGT
            self.show_exams_screen()
        if 340 < x < 460 and 130 < y < 305:
            print("BLHD")
            ExamSetting.selected_subject = Exam.BLHD
            self.show_exams_screen()
        if 610 < x < 730 and 130 < y < 305:
            print("XHTD")
            ExamSetting.selected_subject = Exam.XHTD
            self.show_exams_screen()
        if 95 < x < 225 and 340 < y < 520:
            print("GDGT")
            ExamSetting.selected_subject = Exam.GDGT
            self.show_exams_screen()
        if 340 < x < 460 and 340 < y < 520:
            print("ATM")
            ExamSetting.selected_subject = Exam.ATM
            self.show_exams_screen()
        if 610 < x < 730 and 340 < y < 520:
            print("TLDT")
            ExamSetting.selected_subject = Exam.TLDT
            self.show_exams_screen()
