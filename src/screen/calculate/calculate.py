from src.utils.component import Component
from src.utils.constant import ImageUrl, ToolTip
from src.utils.file import FileManager
from src.utils.gif import AnimatedGifCanvas
import tkinter as tk


class CalculateScreen(tk.Frame):
    def __init__(self, master, callback_list, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        self.master = master
        self.show_utility_screen = callback_list["UtilityScreen"]
        self.show_subject_average_screen = callback_list["SubjectAverageScreen"]
        self.show_academic_result_screen = callback_list["AcademicResultScreen"]

        # self.load_widgets()

    def load_widgets(self):
        gif_path = ImageUrl.bg_calculate_screen
        animated_canvas = AnimatedGifCanvas(self, gif_path, self.on_click)
        animated_canvas.pack()

        Component.left_label(self)
        Component.right_button_back(self, self.show_utility_screen)
        Component.right_button_intro(self, ToolTip.calculate_screen)

    def on_click(self, x, y):
        print(f"Clicked on Page at x={x}, y={y}")
        if 30 < x < 735 and 200 < y < 265:
            print("Tính điểm trung bình môn")
            self.show_subject_average_screen()
        if 30 < x < 735 and 350 < y < 415:
            print("Tính kết quả học tập")
            self.show_academic_result_screen()