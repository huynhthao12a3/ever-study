import tkinter as tk

from src.utils.constant import Auth


class Component:
    # User name
    def left_label(self, callback=None):
        label = tk.Label(self, text="Hi, " + Auth.full_name if Auth.login_success else "",
                         font=("Roboto", 12),
                         bg="white", fg="red", borderwidth=2)
        label.place(x=0, y=2)

    # Login
    def right_button_login(self, callback=None):
        button = tk.Button(self, text="Đăng nhập", fg="red", font=("Roboto", 10, "bold"), borderwidth=4,
                           command=callback)
        button.place(x=720, y=2)

    # Come back
    def right_button_back(self, callback=None):
        button = tk.Button(self, text=" Trở về ", fg="red", font=("Roboto", 10, "bold"), borderwidth=4,
                           command=callback)
        button.place(x=736, y=2)
