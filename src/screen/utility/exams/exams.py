import random
from src.utils.component import Component
from src.utils.constant import ImageUrl, Exam, ExamSetting
from src.utils.file import FileManager
import tkinter as tk
from PIL import Image, ImageTk
from src.utils.gif import AnimatedGifCanvas
import os

class ExamsScreen(tk.Frame):
    def __init__(self, master, callback_list, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        self.master = master
        self.show_exam_screen = callback_list["ExamScreen"]
        self.question_data = None
        self.available_questions = list(ExamSetting.selected_subject)  # Tạo một bản sao của danh sách câu hỏi
        self.used_questions = []  # Danh sách lưu trữ các câu hỏi đã sử dụng
        self.answer = None
        self.gif_canvas = None
        self.file_manager = FileManager()
        self.answer_selected = False  # Thêm biến để theo dõi trạng thái đã chọn đáp án

    def load_widgets(self):
        print("load_widgets", ExamSetting.selected_subject)
        self.available_questions = list(ExamSetting.selected_subject)
        # Chọn câu hỏi đầu tiên
        self.load_new_question()
        # Hiển thị câu hỏi đầu tiên từ image_path
        # self.display_question_image()  # Hiển thị câu hỏi ngay khi tải widget

        Component.right_button_back(self, self.show_exam_screen)

    def on_click(self, x, y):
        print(f"Clicked on Page at x={x}, y={y}")

        if self.answer_selected:
            # Nếu đã chọn đáp án, click tiếp theo sẽ chuyển sang câu hỏi mới
            self.load_new_question()
            return

        # Xác định đáp án dựa trên tọa độ nhấp chuột
        if 675 < x < 755 and 145 < y < 220:  # Vùng cho A
            self.answer = 'A'
            self.answer_selected = True  # Đánh dấu đã chọn đáp án
            print("Selected answer: A")
            self.display_question_image()
        elif 675 < x < 755 and 245 < y < 320:  # Vùng cho B
            self.answer = 'B'
            self.answer_selected = True  # Đánh dấu đã chọn đáp án
            print("Selected answer: B")
            self.display_question_image()
        elif 675 < x < 755 and 350 < y < 430:  # Vùng cho C
            self.answer = 'C'
            self.answer_selected = True  # Đánh dấu đã chọn đáp án
            print("Selected answer: C")
            self.display_question_image()
        elif 675 < x < 755 and 465 < y < 545:  # Vùng cho D
            self.answer = 'D'
            self.answer_selected = True  # Đánh dấu đã chọn đáp án
            print("Selected answer: D")
            self.display_question_image()
        else:
            print("Clicked outside the answer area.")

    def display_question_image(self):
        print("display_question_image")
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

    def load_new_question(self):
        if not self.available_questions:
            print("All questions have been used.")
            self.answer = None
            self.gif_canvas.destroy()
            self.show_exam_screen()
            return

        # Chọn ngẫu nhiên một câu hỏi từ danh sách có sẵn
        new_question = random.choice(self.available_questions)

        # Loại bỏ câu hỏi đã chọn khỏi danh sách có sẵn
        self.available_questions.remove(new_question)

        # Thêm câu hỏi mới vào danh sách đã sử dụng
        self.used_questions.append(new_question)

        # Cập nhật dữ liệu câu hỏi và đặt lại đáp án
        self.question_data = new_question
        self.answer = None
        self.answer_selected = False  # Đặt lại trạng thái chọn đáp án

        print("Loading new question...")
        self.display_question_image()
