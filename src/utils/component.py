import tkinter as tk
from PIL import Image, ImageTk
from src.utils.constant import Auth
from src.utils.file import FileManager


class Component:
    # User name
    def left_label(self, callback=None):
        label = tk.Label(self, text="Hi, " + Auth.full_name if Auth.login_success else "",
                         font=("Roboto", 12),
                         bg="white", fg="red", borderwidth=2)
        label.place(x=0, y=2)

    # Login
    def right_button_login(self, callback=None):
        # button = tk.Button(self, text="Đăng nhập", fg="red", font=("Roboto", 10, "bold"), borderwidth=4,
        #                    command=callback)
        # button.place(x=720, y=2)
        icon = Image.open(FileManager().resource_path("image/setting/login_icon.png"))
        icon = icon.resize((60, 30), Image.LANCZOS)
        self.login_icon = ImageTk.PhotoImage(icon)

        # Tạo nút với icon
        self.login_button = tk.Button(
            self,
            image=self.login_icon,
            command=callback,
            borderwidth=0,
            highlightthickness=0
        )
        self.login_button.place(x=736, y=4)

    # Come back
    def right_button_back(self, callback=None):
        # button = tk.Button(self, text=" Trở về ", fg="red", font=("Roboto", 10, "bold"), borderwidth=4,
        #                    command=callback)
        # button.place(x=736, y=2)
        icon = Image.open(FileManager().resource_path("image/setting/back_icon.png"))
        icon = icon.resize((60, 30), Image.LANCZOS)
        self.back_icon = ImageTk.PhotoImage(icon)

        # Tạo nút với icon
        self.back_button = tk.Button(
            self,
            image=self.back_icon,
            command=callback,
            borderwidth=0,
            highlightthickness=0
        )
        self.back_button.place(x=736, y=4)
