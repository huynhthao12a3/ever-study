from src.utils.component import Component
from src.utils.constant import ImageUrl, ToolTip
from src.utils.file import FileManager
from src.utils.gif import AnimatedGifCanvas
import tkinter as tk


class SubjectScreen(tk.Frame):
    def __init__(self, master, callback_list, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        self.master = master
        self.show_question_bank_screen = callback_list["QuestionBankScreen"]
        self.show_utility_screen = callback_list["UtilityScreen"]

    def load_widgets(self):
        gif_path = ImageUrl.bg_subject_screen
        animated_canvas = AnimatedGifCanvas(self, gif_path, self.on_click)
        animated_canvas.pack()

        Component.left_label(self)
        Component.right_button_back(self, self.show_question_bank_screen)

    def on_click(self, x, y):
        print(f"Clicked on Page at x={x}, y={y}")
