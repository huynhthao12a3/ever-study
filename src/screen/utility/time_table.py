import tkinter as tk
from tkinter import messagebox, filedialog
import cairo
import os
from PIL import Image, ImageTk
from src.utils.component import Component
from src.utils.constant import ImageUrl, Color, Font
from src.utils.file import FileManager

class TimeTableScreen(tk.Frame):
    def __init__(self, master, callback_list, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.master = master
        self.show_home_screen = callback_list["HomeScreen"]
        self.show_time_table_screen = callback_list["UtilityScreen"]

        self.days = ['Thứ 2', 'Thứ 3', 'Thứ 4', 'Thứ 5', 'Thứ 6']
        self.time_slots = [''] * 10
        self.entries = {}
        self.time_entries = {}

        self.positions = {
            ('Thứ 2', 0): (100, 100), ('Thứ 3', 0): (200, 100), ('Thứ 4', 0): (300, 100), ('Thứ 5', 0): (400, 100),
            ('Thứ 6', 0): (500, 100),
            ('Thứ 2', 1): (100, 150), ('Thứ 3', 1): (200, 150), ('Thứ 4', 1): (300, 150), ('Thứ 5', 1): (400, 150),
            ('Thứ 6', 1): (500, 150),
            ('Thứ 2', 2): (100, 200), ('Thứ 3', 2): (200, 200), ('Thứ 4', 2): (300, 200), ('Thứ 5', 2): (400, 200),
            ('Thứ 6', 2): (500, 200),
            ('Thứ 2', 3): (100, 250), ('Thứ 3', 3): (200, 250), ('Thứ 4', 3): (300, 250), ('Thứ 5', 3): (400, 250),
            ('Thứ 6', 3): (500, 250),
            ('Thứ 2', 4): (100, 300), ('Thứ 3', 4): (200, 300), ('Thứ 4', 4): (300, 300), ('Thứ 5', 4): (400, 300),
            ('Thứ 6', 4): (500, 300),
            ('Thứ 2', 5): (100, 350), ('Thứ 3', 5): (200, 350), ('Thứ 4', 5): (300, 350), ('Thứ 5', 5): (400, 350),
            ('Thứ 6', 5): (500, 350),
            ('Thứ 2', 6): (100, 400), ('Thứ 3', 6): (200, 400), ('Thứ 4', 6): (300, 400), ('Thứ 5', 6): (400, 400),
            ('Thứ 6', 6): (500, 400),
            ('Thứ 2', 7): (100, 450), ('Thứ 3', 7): (200, 450), ('Thứ 4', 7): (300, 450), ('Thứ 5', 7): (400, 450),
            ('Thứ 6', 7): (500, 450),
            ('Thứ 2', 8): (100, 500), ('Thứ 3', 8): (200, 500), ('Thứ 4', 8): (300, 500), ('Thứ 5', 8): (400, 500),
            ('Thứ 6', 8): (500, 500),
            ('Thứ 2', 9): (100, 550), ('Thứ 3', 9): (200, 550), ('Thứ 4', 9): (300, 550), ('Thứ 5', 9): (400, 550),
            ('Thứ 6', 9): (500, 550),
        }

        self.background_path1 = FileManager().resource_path(ImageUrl.bg_time_table_child1_screen)
        self.background_path2 = FileManager().resource_path(ImageUrl.bg_time_table_child2_screen)
        self.current_background = self.background_path1
        self.slots_to_print = 10  # Default to 10 slots

        # Load the background image
        self.bg_image = Image.open(FileManager().resource_path(ImageUrl.bg_time_table_screen))
        self.bg_photo = ImageTk.PhotoImage(self.bg_image)

        self.load_widgets()

    def load_widgets(self):
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # Create a label with the background image
        self.bg_label = tk.Label(self, image=self.bg_photo)
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        main_frame = tk.Frame(self, bg=Color.bg_color_blue)
        main_frame.place(relx=0.5, rely=0.5, anchor='center', relwidth=0.8, relheight=0.8)

        grid_frame = tk.Frame(main_frame, bg=Color.bg_color_blue)
        grid_frame.pack(expand=True, fill='both', padx=10, pady=10)

        for i in range(12):  # 10 slots + 1 header + 1 for buttons
            grid_frame.grid_rowconfigure(i, weight=1)
        for i in range(7):  # 5 days + 1 time column + 1 for padding
            grid_frame.grid_columnconfigure(i, weight=1)

        tk.Label(grid_frame, text="Thời gian", bg=Color.bg_color_blue, font=Font.main_font_mold).grid(row=0, column=1,
                                                                                                      sticky="nsew")
        for i, day in enumerate(self.days):
            tk.Label(grid_frame, text=day, bg=Color.bg_color_blue, font=Font.main_font_mold).grid(row=0, column=i + 2,
                                                                                                  sticky="nsew")

        for i in range(10):
            tk.Label(grid_frame, bg=Color.bg_color_blue).grid(row=i + 1, column=0, sticky="nsew")
            self.time_entries[i] = tk.Entry(grid_frame)
            self.time_entries[i].grid(row=i + 1, column=1, sticky="nsew", padx=2, pady=2)
            for j, day in enumerate(self.days):
                self.entries[(day, i)] = tk.Entry(grid_frame)
                self.entries[(day, i)].grid(row=i + 1, column=j + 2, sticky="nsew", padx=2, pady=2)

        bg_frame = tk.Frame(grid_frame, bg=Color.bg_color_blue)
        bg_frame.grid(row=11, column=0, columnspan=7, pady=10)

        bg_image1 = Image.open(self.background_path1)
        bg_image2 = Image.open(self.background_path2)

        bg_image1.thumbnail((100, 100))
        bg_image2.thumbnail((100, 100))

        self.bg_photo1 = ImageTk.PhotoImage(bg_image1)
        self.bg_photo2 = ImageTk.PhotoImage(bg_image2)

        bg_label_1 = tk.Label(bg_frame, image=self.bg_photo1, bg="white")
        bg_label_1.bind("<Button-1>", lambda event: self.set_background(self.background_path1, 10))

        bg_label_2 = tk.Label(bg_frame, image=self.bg_photo2, bg="white")
        bg_label_2.bind("<Button-1>", lambda event: self.set_background(self.background_path2, 5))

        bg_label_1.grid(row=0, column=0, padx=10)
        bg_label_2.grid(row=0, column=1, padx=10)

        tk.Button(bg_frame, text="Tạo ảnh thời khóa biểu", command=self.generate_image).grid(row=1, columnspan=2,
                                                                                             pady=(10))

        Component.left_label(self)
        Component.right_button_back(self, self.show_time_table_screen)

    def set_background(self, bg_path, slots):
        self.current_background = bg_path
        self.slots_to_print = slots
        messagebox.showinfo("Thông báo", f"Đã chọn nền: {os.path.basename(bg_path).split(".")[0]}. Sẽ in {slots} slot khi tạo ảnh.")

    def generate_image(self):
        try:
            # Mở hộp thoại để chọn nơi lưu file
            output_path = filedialog.asksaveasfilename(
                defaultextension=".png",
                filetypes=[("PNG files", "*.png"), ("All files", "*.*")],
                title="Chọn nơi lưu ảnh thời khóa biểu"
            )

            # Nếu người dùng không chọn nơi lưu (nhấn Cancel), thoát khỏi hàm
            if not output_path:
                return

            background_image = Image.open(self.current_background)
            width, height = background_image.size
            surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, width, height)
            ctx = cairo.Context(surface)

            img = background_image.convert('RGBA')
            img_data = bytearray(img.tobytes('raw', 'BGRA'))
            image = cairo.ImageSurface.create_for_data(img_data, cairo.FORMAT_ARGB32, width, height)
            ctx.set_source_surface(image, 0, 0)
            ctx.paint()

            ctx.select_font_face("Arial", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_NORMAL)
            ctx.set_source_rgb(0, 0, 0)
            ctx.set_font_size(16)

            for i in range(self.slots_to_print):
                time = self.time_entries[i].get()
                ctx.move_to(50, 100 + i * 50)  # Vị trí cho cột thời gian
                ctx.show_text(time)
                for day in self.days:
                    subject = self.entries[(day, i)].get()
                    x, y = self.positions[(day, i)]
                    ctx.move_to(x, y)
                    ctx.show_text(subject)

            surface.write_to_png(output_path)
            messagebox.showinfo("Thành công", f"Đã lưu ảnh tại: {output_path}")
            os.startfile(output_path)

        except Exception as e:
            messagebox.showerror("Lỗi", f"Đã xảy ra lỗi: {str(e)}")