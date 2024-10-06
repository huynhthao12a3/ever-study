from src.utils.component import Component
from src.utils.constant import Auth, ImageUrl, FileUrl
from src.utils.file import FileManager
from src.utils.gif import AnimatedGifCanvas
import tkinter as tk
import webbrowser

class MathScreen(tk.Frame):
    def __init__(self, master, callback_list, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        self.master = master
        self.show_learn_screen = callback_list["LearnScreen"]
        self.file_manager = FileManager()
        # self.load_widgets()

    def load_widgets(self):
        gif_path = ImageUrl.bg_math_screen
        animated_canvas = AnimatedGifCanvas(self, gif_path, self.on_click)
        animated_canvas.pack()

        Component.left_label(self)
        Component.right_button_back(self, self.show_learn_screen)

    def on_click(self, x, y):
        print(f"Clicked on Page at x={x}, y={y}")
        # webbrowser.open(FileManager().resource_path('CV_Huynh-Van-Thao.pdf'))

        if 60 < x < 430 and 144 < y < 164:
            print("Chuong 1")
            webbrowser.open(self.file_manager.resource_path("file/math/" + FileUrl.f_toan_chuong_01))
        if 60 < x < 635 and 190 < y < 210:
            print("Chuong 2")
            webbrowser.open(self.file_manager.resource_path("file/math/" + FileUrl.f_toan_chuong_02))
        if 60 < x < 460 and 238 < y < 256:
            print("Chuong 3")
            webbrowser.open(self.file_manager.resource_path("file/math/" + FileUrl.f_toan_chuong_03))
        if 60 < x < 540 and 284 < y < 305:
            print("Chuong 4")
            webbrowser.open(self.file_manager.resource_path("file/math/" + FileUrl.f_toan_chuong_04))
        if 60 < x < 445 and 328 < y < 350:
            print("Chuong 5")
            webbrowser.open(self.file_manager.resource_path("file/math/" + FileUrl.f_toan_chuong_05))
        if 60 < x < 400 and 377 < y < 396:
            print("Chuong 6")
            webbrowser.open(self.file_manager.resource_path("file/math/" + FileUrl.f_toan_chuong_06))
        if 60 < x < 400 and 424 < y < 445:
            print("Chuong 7")
            webbrowser.open(self.file_manager.resource_path("file/math/" + FileUrl.f_toan_chuong_07))
        if 60 < x < 430 and 470 < y < 490:
            print("Chuong 8")
            webbrowser.open(self.file_manager.resource_path("file/math/" + FileUrl.f_toan_chuong_08))
        if 60 < x < 535 and 515 < y < 540:
            print("Chuong 9")
            webbrowser.open(self.file_manager.resource_path("file/math/" + FileUrl.f_toan_chuong_09))
