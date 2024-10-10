import random
from src.utils.component import Component
from src.utils.constant import ImageUrl, Exam
from src.utils.file import FileManager
import tkinter as tk
from PIL import Image, ImageTk
from src.utils.gif import AnimatedGifCanvas
import os

class TrafficSafetyScreen(tk.Frame):
    def __init__(self, master, callback_list, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        self.master = master
        self.show_utility_screen = callback_list["UtilityScreen"]
        self.question_data = None  # Khởi tạo biến cho câu hỏi
        self.used_questions = []    # Danh sách lưu trữ các câu hỏi đã sử dụng
        self.answer = None          # Đáp án mặc định là None
        self.gif_canvas = None      # Biến để lưu AnimatedGifCanvas
        self.file_manager = FileManager()

        # Chọn câu hỏi đầu tiên
        self.load_new_question()

    def load_widgets(self):
        # Hiển thị câu hỏi đầu tiên từ image_path
        self.display_question_image()  # Hiển thị câu hỏi ngay khi tải widget

        Component.right_button_back(self, self.show_utility_screen)

    def on_click(self, x, y):
        print(f"Clicked on Page at x={x}, y={y}")

        # Xác định đáp án dựa trên tọa độ nhấp chuột
        if 20 < x < 520 and 184 < y < 235:  # Vùng cho A
            self.answer = 'A'
            print("Selected answer: A")
            self.display_question_image()
        elif 20 < x < 520 and 260 < y < 315:  # Vùng cho B
            self.answer = 'B'
            print("Selected answer: B")
            self.display_question_image()
        elif 20 < x < 520 and 335 < y < 385:  # Vùng cho C
            self.answer = 'C'
            print("Selected answer: C")
            self.display_question_image()
        elif 20 < x < 520 and 420 < y < 475:  # Vùng cho D
            self.answer = 'D'
            print("Selected answer: D")
            self.display_question_image()
        else:
            print("Clicked outside the answer area.")

    def display_question_image(self):
        if not self.answer:
            # Hiển thị hình ảnh câu hỏi ban đầu từ image_path nếu chưa chọn đáp án
            image_path = self.question_data["image_path"]
        else:
            # Hiển thị hình ảnh theo đáp án đã chọn
            image_path = self.question_data[self.answer]

        print("Image Path: ", image_path)  # In ra đường dẫn để kiểm tra

        # Sử dụng AnimatedGifCanvas để hiển thị hình ảnh câu hỏi
        if self.gif_canvas:
            self.gif_canvas.destroy()  # Xóa canvas cũ nếu có

        self.gif_canvas = AnimatedGifCanvas(self, image_path, self.on_click)
        self.gif_canvas.pack()

        if self.answer:
            # Gọi phương thức chuyển sang câu hỏi mới sau 5 giây nếu đã chọn đáp án
            self.after(5000, self.load_new_question)


    def load_new_question(self):
        if len(self.used_questions) >= len(Exam.ATGT):
            print("All questions have been used.")
            return

        while True:
            new_question = random.choice(Exam.ATGT)
            if new_question not in self.used_questions:
                break

        # Thêm câu hỏi mới vào danh sách đã sử dụng
        self.used_questions.append(new_question)

        # Cập nhật dữ liệu câu hỏi và đặt lại đáp án
        self.question_data = new_question
        self.answer = None

        print("Loading new question...")

        # Hiển thị hình ảnh câu hỏi mới
        self.display_question_image()

# Sử dụng class TrafficSafetyScreen trong ứng dụng của bạn.