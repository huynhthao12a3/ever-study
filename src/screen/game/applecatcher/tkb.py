import tkinter as tk
from tkinter import messagebox
import cairo
import os
from PIL import Image, ImageTk

from src.utils.file import FileManager


class TimetableApp:
    def __init__(self, master):
        self.master = master
        master.title("Tạo ảnh Thời khóa biểu")

        self.days = ['Thứ 2', 'Thứ 3', 'Thứ 4', 'Thứ 5', 'Thứ 6']
        self.time_slots = ['', '', '', '', '']
        self.entries = {}
        self.time_entries = {}

        # Thiết lập vị trí mặc định cho các ô nhập
        self.positions = {
            ('Thứ 2', 0): (100, 100), ('Thứ 3', 0): (200, 100), ('Thứ 4', 0): (300, 100), ('Thứ 5', 0): (400, 100), ('Thứ 6', 0): (500, 100),
            ('Thứ 2', 1): (100, 150), ('Thứ 3', 1): (200, 150), ('Thứ 4', 1): (300, 150), ('Thứ 5', 1): (400, 150), ('Thứ 6', 1): (500, 150),
            ('Thứ 2', 2): (100, 200), ('Thứ 3', 2): (200, 200), ('Thứ 4', 2): (300, 200), ('Thứ 5', 2): (400, 200), ('Thứ 6', 2): (500, 200),
            ('Thứ 2', 3): (100, 250), ('Thứ 3', 3): (200, 250), ('Thứ 4', 3): (300, 250), ('Thứ 5', 3): (400, 250), ('Thứ 6', 3): (500, 250),
            ('Thứ 2', 4): (100, 300), ('Thứ 3', 4): (200, 300), ('Thứ 4', 4): (300, 300), ('Thứ 5', 4): (400, 300), ('Thứ 6', 4): (500, 300),
        }

        # Đặt đường dẫn cố định cho ảnh nền
        self.background_path = FileManager().resource_path('image/background/game.png')
        self.background_image = Image.open(self.background_path)

        # Frame cho các điều khiển
        control_frame = tk.Frame(master)
        control_frame.pack(side=tk.LEFT, padx=10, pady=10)

        # Frame cho grid layout
        grid_frame = tk.Frame(control_frame)
        grid_frame.pack()

        # Frame cho preview ảnh
        self.preview_frame = tk.Frame(master)
        self.preview_frame.pack(side=tk.RIGHT, padx=10, pady=10)

        tk.Label(grid_frame, text="Thời gian").grid(row=0, column=1)
        for i, day in enumerate(self.days):
            tk.Label(grid_frame, text=day).grid(row=0, column=i+2)

        for i in range(5):
            tk.Label(grid_frame, text=f"Slot {i+1}").grid(row=i+1, column=0)
            self.time_entries[i] = tk.Entry(grid_frame, width=15)
            self.time_entries[i].grid(row=i+1, column=1)
            for j, day in enumerate(self.days):
                self.entries[(day, i)] = tk.Entry(grid_frame, width=15)
                self.entries[(day, i)].grid(row=i+1, column=j+2)

        tk.Button(control_frame, text="Tạo ảnh thời khóa biểu", command=self.generate_image).pack()

        self.preview_label = tk.Label(self.preview_frame)
        self.preview_label.pack()

        # Hiển thị preview của ảnh nền
        self.update_preview()

    def update_preview(self):
        preview = self.background_image.copy()
        preview.thumbnail((400, 400))
        photo = ImageTk.PhotoImage(preview)
        self.preview_label.config(image=photo)
        self.preview_label.image = photo

    def generate_image(self):
        try:
            width, height = self.background_image.size
            surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, width, height)
            ctx = cairo.Context(surface)

            # Vẽ ảnh nền
            img = Image.open(self.background_path).convert('RGBA')
            img_data = bytearray(img.tobytes('raw', 'BGRA'))
            image = cairo.ImageSurface.create_for_data(img_data, cairo.FORMAT_ARGB32, width, height)
            ctx.set_source_surface(image, 0, 0)
            ctx.paint()

            # Thiết lập font và màu cho text
            ctx.select_font_face("Arial", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_NORMAL)
            ctx.set_source_rgb(0, 0, 0)
            ctx.set_font_size(16)

            # Vẽ thời khóa biểu
            for i in range(5):
                time = self.time_entries[i].get()
                for j, day in enumerate(self.days):
                    subject = self.entries[(day, i)].get()
                    x, y = self.positions[(day, i)]
                    ctx.move_to(x, y)
                    ctx.show_text(f"{time}: {subject}")

            # Lưu ảnh
            output_path = "output_timetable.png"
            surface.write_to_png(output_path)
            messagebox.showinfo("Thành công", f"Đã lưu ảnh tại: {output_path}")
            os.startfile(output_path)

        except Exception as e:
            messagebox.showerror("Lỗi", f"Đã xảy ra lỗi: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = TimetableApp(root)
    root.mainloop()