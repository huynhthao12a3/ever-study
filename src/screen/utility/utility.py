import os
from tkinter import messagebox

from src.utils.component import Component
from src.utils.constant import ImageUrl, ToolTip
from src.utils.file import FileManager
from src.utils.gif import AnimatedGifCanvas
import tkinter as tk
from tkinter import filedialog, messagebox
import subprocess
import psutil  # Cần cài đặt: pip install psutil
import threading
import time
import psutil
import win32gui  # pip install pywin32
import win32process


class UtilityScreen(tk.Frame):
    def __init__(self, master, callback_list, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        self.master = master
        self.show_home_screen = callback_list["HomeScreen"]
        self.show_calculate_screen = callback_list["CalculateScreen"]
        self.show_time_table_screen = callback_list["TimeTableScreen"]
        self.show_exam_screen = callback_list["ExamScreen"]
        self.show_chat_ai_screen = callback_list["ChatAIScreen"]
        self.show_question_bank_screen = callback_list["QuestionBankScreen"]
        self.is_powerpoint_open = False
        self.powerpoint_hwnd = None

    def load_widgets(self):
        gif_path = ImageUrl.bg_utility_screen
        animated_canvas = AnimatedGifCanvas(self, gif_path, self.on_click)
        animated_canvas.pack()

        # Handle change cursor
        animated_canvas.add_clickable_area(95, 135, 245, 325)  # Calculate Screen
        animated_canvas.add_clickable_area(335, 135, 485, 325)  # Time Table Screen
        animated_canvas.add_clickable_area(575, 135, 730, 325)  # Updating...
        animated_canvas.add_clickable_area(95, 365, 245, 535)  # Exam Screen
        animated_canvas.add_clickable_area(300, 365, 520, 535)  # Open .ppsm
        animated_canvas.add_clickable_area(575, 365, 730, 535)  # Chat AI Screen

        Component.left_label(self)
        Component.right_button_back(self, self.show_home_screen)
        Component.right_button_intro(self, ToolTip.utility_screen)

    def on_click(self, x, y):
        print(f"Clicked on Page at x={x}, y={y}")
        if 95 < x < 245 and 135 < y < 325:
            self.show_calculate_screen()
        if 335 < x < 485 and 135 < y < 325:
            self.show_time_table_screen()
        if 575 < x < 730 and 135 < y < 325:
            self.show_question_bank_screen()
            # messagebox.showinfo("Thông báo", f"Tính năng này đang phát trển.\nVui lòng quay lại sau.")
        if 95 < x < 245 and 365 < y < 535:
            self.show_exam_screen()
        if 300 < x < 520 and 365 < y < 535:
            if not self.is_powerpoint_open:
                self.open_ppsm_file(FileManager().resource_path("slide/kham-pha-Viet-Nam.ppsm"))
            else:
                messagebox.showinfo("Thông báo",
                                    "Một file PowerPoint đang được mở.\nVui lòng đóng nó trước khi mở file mới.")
        if 575 < x < 730 and 365 < y < 535:
            self.show_chat_ai_screen()

    def open_ppsm_file(self, file_path):
        if self.is_powerpoint_open:
            messagebox.showinfo("Thông báo",
                                "Một file PowerPoint đang được mở.\nVui lòng đóng nó trước khi mở file mới.")
            return

        try:
            os.startfile(file_path)
            self.is_powerpoint_open = True
            messagebox.showinfo("Thông báo", "PowerPoint đang được mở.\nVui lòng đợi...")
            threading.Thread(target=self.find_powerpoint_window, daemon=True).start()

        except Exception as e:
            messagebox.showerror("Lỗi", f"Không thể mở file: {e}")

    def find_powerpoint_window(self):
        # time.sleep(2)  # Đợi PowerPoint khởi động

        def callback(hwnd, hwnds):
            if win32gui.IsWindowVisible(hwnd) and win32gui.IsWindowEnabled(hwnd):
                _, pid = win32process.GetWindowThreadProcessId(hwnd)
                try:
                    process = psutil.Process(pid)
                    if process.name().lower() == "powerpnt.exe" or process.name().lower() == "powerpoint.exe":
                        hwnds.append(hwnd)
                except psutil.NoSuchProcess:
                    pass
            return True

        hwnds = []
        win32gui.EnumWindows(callback, hwnds)

        if hwnds:
            self.powerpoint_hwnd = hwnds[0]
            self.check_powerpoint_status()
        else:
            self.is_powerpoint_open = False

    def check_powerpoint_status(self):
        while self.is_powerpoint_open:
            if not win32gui.IsWindow(self.powerpoint_hwnd) or not win32gui.IsWindowVisible(self.powerpoint_hwnd):
                self.is_powerpoint_open = False
                print("powerpoint đã đóng .................................")
                # messagebox.showinfo("Thông báo", "PowerPoint đã được đóng.")
                break
            # time.sleep(1)
