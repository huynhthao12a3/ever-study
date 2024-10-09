import tkinter as tk
from tkinter import messagebox, filedialog
import cairo
import os
from PIL import Image, ImageTk
from src.utils.component import Component
from src.utils.constant import ImageUrl, Color, Font, Auth
from src.utils.file import FileManager


class TimeTableScreen(tk.Frame):
    def __init__(self, master, callback_list, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.master = master
        self.show_home_screen = callback_list["HomeScreen"]
        self.show_utility_screen = callback_list["UtilityScreen"]

        self.days = ['Thứ 2', 'Thứ 3', 'Thứ 4', 'Thứ 5', 'Thứ 6']
        self.time_slots = [''] * 10
        self.entries = {}
        self.time_entries = {}

        # Positions for 10 slots (background 1)
        self.positions_1 = {
            ('Thứ 2', 0): (190, 105), ('Thứ 3', 0): (300, 105), ('Thứ 4', 0): (410, 105), ('Thứ 5', 0): (520, 105),
            ('Thứ 6', 0): (630, 105),
            ('Thứ 2', 1): (190, 160), ('Thứ 3', 1): (300, 160), ('Thứ 4', 1): (410, 160), ('Thứ 5', 1): (520, 160),
            ('Thứ 6', 1): (630, 160),
            ('Thứ 2', 2): (190, 210), ('Thứ 3', 2): (300, 210), ('Thứ 4', 2): (410, 210), ('Thứ 5', 2): (520, 210),
            ('Thứ 6', 2): (630, 210),
            ('Thứ 2', 3): (190, 260), ('Thứ 3', 3): (300, 260), ('Thứ 4', 3): (410, 260), ('Thứ 5', 3): (520, 260),
            ('Thứ 6', 3): (630, 260),
            ('Thứ 2', 4): (190, 315), ('Thứ 3', 4): (300, 315), ('Thứ 4', 4): (410, 315), ('Thứ 5', 4): (520, 315),
            ('Thứ 6', 4): (630, 315),
            ('Thứ 2', 5): (190, 370), ('Thứ 3', 5): (300, 370), ('Thứ 4', 5): (410, 370), ('Thứ 5', 5): (520, 370),
            ('Thứ 6', 5): (630, 370),
            ('Thứ 2', 6): (190, 420), ('Thứ 3', 6): (300, 420), ('Thứ 4', 6): (410, 420), ('Thứ 5', 6): (520, 420),
            ('Thứ 6', 6): (630, 420),
            ('Thứ 2', 7): (190, 470), ('Thứ 3', 7): (300, 470), ('Thứ 4', 7): (410, 470), ('Thứ 5', 7): (520, 470),
            ('Thứ 6', 7): (630, 470),
            ('Thứ 2', 8): (190, 525), ('Thứ 3', 8): (300, 525), ('Thứ 4', 8): (410, 525), ('Thứ 5', 8): (520, 525),
            ('Thứ 6', 8): (630, 525),
            ('Thứ 2', 9): (190, 580), ('Thứ 3', 9): (300, 580), ('Thứ 4', 9): (410, 580), ('Thứ 5', 9): (520, 580),
            ('Thứ 6', 9): (630, 580),
        }

        # Positions for 5 slots (background 2)
        self.positions_2 = {
            ('Thứ 2', 0): (200, 335), ('Thứ 3', 0): (305, 335), ('Thứ 4', 0): (410, 335), ('Thứ 5', 0): (520, 335),
            ('Thứ 6', 0): (625, 335),
            ('Thứ 2', 1): (200, 390), ('Thứ 3', 1): (305, 390), ('Thứ 4', 1): (410, 390), ('Thứ 5', 1): (520, 390),
            ('Thứ 6', 1): (625, 390),
            ('Thứ 2', 2): (200, 440), ('Thứ 3', 2): (305, 440), ('Thứ 4', 2): (410, 440), ('Thứ 5', 2): (520, 440),
            ('Thứ 6', 2): (625, 440),
            ('Thứ 2', 3): (200, 490), ('Thứ 3', 3): (305, 490), ('Thứ 4', 3): (410, 490), ('Thứ 5', 3): (520, 490),
            ('Thứ 6', 3): (625, 490),
            ('Thứ 2', 4): (200, 540), ('Thứ 3', 4): (305, 540), ('Thứ 4', 4): (410, 540), ('Thứ 5', 4): (520, 540),
            ('Thứ 6', 4): (625, 540),
        }

        # Positions for time column (10 slots)
        self.time_positions_1 = {
            0: (85, 105), 1: (85, 160), 2: (85, 210), 3: (85, 260), 4: (85, 315),
            5: (85, 370), 6: (85, 420), 7: (85, 470), 8: (85, 525), 9: (85, 580),
        }

        # Positions for time column (5 slots)
        self.time_positions_2 = {
            0: (90, 335), 1: (90, 390), 2: (90, 440), 3: (90, 490), 4: (90, 540),
        }

        self.background_path1 = FileManager().resource_path(ImageUrl.bg_time_table_child1_screen)
        self.background_path2 = FileManager().resource_path(ImageUrl.bg_time_table_child2_screen)
        self.current_background = self.background_path1
        self.current_positions = self.positions_1
        self.current_time_positions = self.time_positions_1
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
            self.time_entries[i] = tk.Entry(grid_frame, font=Font.main_font_12)
            self.time_entries[i].grid(row=i + 1, column=1, sticky="nsew", padx=2, pady=2)
            for j, day in enumerate(self.days):
                self.entries[(day, i)] = tk.Entry(grid_frame, font=Font.main_font_12)
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
        bg_label_1.bind("<Button-1>", lambda event: self.set_background(self.background_path1, self.positions_1,
                                                                        self.time_positions_1, 10))

        bg_label_2 = tk.Label(bg_frame, image=self.bg_photo2, bg="white")
        bg_label_2.bind("<Button-1>", lambda event: self.set_background(self.background_path2, self.positions_2,
                                                                        self.time_positions_2, 5))

        bg_label_1.grid(row=0, column=0, padx=10)
        bg_label_2.grid(row=0, column=1, padx=10)

        tk.Button(bg_frame, text="Tạo ảnh thời khóa biểu", font=Font.main_font, command=self.generate_image).grid(row=1,
                                                                                                                  columnspan=2,
                                                                                                                  pady=(
                                                                                                                      10))

        Component.left_label(self)
        Component.right_button_back(self, self.show_utility_screen)

    def set_background(self, bg_path, positions, time_positions, slots):
        self.current_background = bg_path
        self.current_positions = positions
        self.current_time_positions = time_positions
        self.slots_to_print = slots
        messagebox.showinfo("Thông báo", f"Đã chọn nền: {os.path.basename(bg_path)}. Sẽ in {slots} hàng khi tạo ảnh.")

    def generate_image(self):
        try:
            output_path = filedialog.asksaveasfilename(
                defaultextension=".png",
                filetypes=[("PNG files", "*.png"), ("All files", "*.*")],
                title="Chọn nơi lưu ảnh thời khóa biểu"
            )

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

            ctx.select_font_face(Font.main_font, cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_NORMAL)
            ctx.set_source_rgb(0, 0, 0)
            if self.slots_to_print == 5:
                ctx.set_font_size(24)
                ctx.move_to(40, 92)
                ctx.show_text(Auth.full_name)
            ctx.set_font_size(16)
            for i in range(self.slots_to_print):
                time = self.time_entries[i].get()
                x, y = self.current_time_positions[i]
                ctx.move_to(x, y)
                ctx.show_text(time)
                for day in self.days:
                    subject = self.entries[(day, i)].get()
                    x, y = self.current_positions[(day, i)]
                    ctx.move_to(x, y)
                    ctx.show_text(subject)

            surface.write_to_png(output_path)
            messagebox.showinfo("Thành công", f"Đã lưu ảnh tại: {output_path}")
            os.startfile(output_path)

        except Exception as e:
            messagebox.showerror("Lỗi", f"Đã xảy ra lỗi: {str(e)}")
