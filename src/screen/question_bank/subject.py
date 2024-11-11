import webbrowser
from tkinter import messagebox

from src.utils.component import Component
from src.utils.constant import ImageUrl, ToolTip, AppSetting
from src.utils.file import FileManager
from src.utils.gif import AnimatedGifCanvas
import tkinter as tk


class SubjectScreen(tk.Frame):
    def __init__(self, master, callback_list, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        self.master = master
        self.show_question_bank_screen = callback_list["QuestionBankScreen"]
        self.show_utility_screen = callback_list["UtilityScreen"]
        self.file_manager = FileManager()

    def load_widgets(self):
        gif_path = ImageUrl.bg_subject_screen
        animated_canvas = AnimatedGifCanvas(self, gif_path, self.on_click)
        animated_canvas.pack()

        # Handle change cursor
        animated_canvas.add_clickable_area(65, 140, 130, 225)
        animated_canvas.add_clickable_area(148, 140, 212, 225)
        animated_canvas.add_clickable_area(230, 140, 295, 225)
        animated_canvas.add_clickable_area(310, 140, 375, 225)
        animated_canvas.add_clickable_area(435, 140, 500, 225)
        animated_canvas.add_clickable_area(520, 140, 582, 225)
        animated_canvas.add_clickable_area(600, 140, 665, 225)
        animated_canvas.add_clickable_area(680, 140, 745, 225)

        Component.left_label(self)
        Component.right_button_back(self, self.show_question_bank_screen)

    def on_click(self, x, y):
        print(f"Clicked on Page at x={x}, y={y}")
        if 65 < x < 130 and 140 < y < 225:
            messagebox.showinfo("Thông báo", "Ứng dụng đang trong quá trình chuẩn bị tài liệu.\nVui lòng quay lại sau.")
            # webbrowser.open(self.file_manager.resource_path("file/kho-de/" + AppSetting.utility_instance["ghk1"]))
        if 148 < x < 212 and 140 < y < 225:
            messagebox.showinfo("Thông báo", "Ứng dụng đang trong quá trình chuẩn bị tài liệu.\nVui lòng quay lại sau.")
            # webbrowser.open(self.file_manager.resource_path("file/kho-de/" + AppSetting.utility_instance["hk1"]))
        if 230 < x < 295 and 140 < y < 225:
            messagebox.showinfo("Thông báo", "Ứng dụng đang trong quá trình chuẩn bị tài liệu.\nVui lòng quay lại sau.")
            # webbrowser.open(self.file_manager.resource_path("file/kho-de/" + AppSetting.utility_instance["ghk2"]))
        if 310 < x < 375 and 140 < y < 225:
            webbrowser.open(self.file_manager.resource_path("file/kho-de/" + AppSetting.subject_instance["hk2"]))

        if 435 < x < 500 and 140 < y < 225:
            messagebox.showinfo("Thông báo", "Ứng dụng đang trong quá trình chuẩn bị tài liệu.\nVui lòng quay lại sau.")
            # webbrowser.open(self.file_manager.resource_path("file/kho-de/" + AppSetting.utility_instance["ghk1"]))
        if 520 < x < 582 and 140 < y < 225:
            messagebox.showinfo("Thông báo", "Ứng dụng đang trong quá trình chuẩn bị tài liệu.\nVui lòng quay lại sau.")
            # webbrowser.open(self.file_manager.resource_path("file/kho-de/" + AppSetting.utility_instance["hk1"]))
        if 600 < x < 665 and 140 < y < 225:
            messagebox.showinfo("Thông báo", "Ứng dụng đang trong quá trình chuẩn bị tài liệu.\nVui lòng quay lại sau.")
            # webbrowser.open(self.file_manager.resource_path("file/kho-de/" + AppSetting.utility_instance["ghk2"]))
        if 680 < x < 745 and 140 < y < 225:
            messagebox.showinfo("Thông báo", "Ứng dụng đang trong quá trình chuẩn bị tài liệu.\nVui lòng quay lại sau.")
            # webbrowser.open(self.file_manager.resource_path("file/kho-de/" + AppSetting.utility_instance["hk2"]))
