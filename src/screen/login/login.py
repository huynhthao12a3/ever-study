import tkinter as tk
from tkinter import font
import pygame.display

from src.utils.component import Component
from src.utils.constant import Auth, Api, ImageUrl, Font
# from tkextrafont import Font
from src.utils.file import FileManager
# Call api, convert json library
import requests
import json

from src.utils.gif import AnimatedGifCanvas
from src.utils.popup import ErasablePopup


class LoginScreen(tk.Frame):
    def __init__(self, master, callback_list, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        self.master = master
        self.show_home_screen = callback_list["HomeScreen"]

        # Variable
        self.username_verify = tk.StringVar()
        self.password_verify = tk.StringVar()
        self.username_login_entry = None
        self.password_login_entry = None
        self.login_success_screen = None

        # self.load_widgets()

    def load_widgets(self):
        gif_path = ImageUrl.bg_login_screen
        animated_canvas = AnimatedGifCanvas(self, gif_path, self.on_click)
        animated_canvas.pack()

        custom_font = tk.font.Font(family=Font.main_font, size=16)
        Component.right_button_back(self, self.show_home_screen)

        self.username_login_entry = tk.Entry(self, textvariable=self.username_verify, borderwidth=3, font=custom_font)
        self.username_login_entry.place(x=340, y=222, height=40, width=310)

        self.password_login_entry = tk.Entry(self, textvariable=self.password_verify, show='*', borderwidth=3, font=custom_font)
        self.password_login_entry.place(x=340, y=312, height=40, width=310)

    def on_click(self, x, y):
        print(f"Clicked on Page at x={x}, y={y}")
        if 300 < x < 600 and 450 < y < 520 :
            print("Login")
            self.login_verify()

    # Implementing event on login button

    def login_verify(self):
        username = self.username_verify.get()
        password = self.password_verify.get()

        # defining the api-endpoint
        api_endpoint = Api.api_endpoint + "/login"
        headers = {'Content-Type': 'application/json'}
        data = {
            "username": username,   # "huynhthao@gmail.com",
            "password": password    # "123456"
        }

        response = None
        response_json = None
        # cal api
        try:
            response = requests.post(url=api_endpoint, json=data, headers=headers)
            response_json = response.json()
        except Exception as e:
            print(e)
            tk.Label(self, text="Đăng nhập thất bại", width=16, font=(Font.main_font, 16, 'bold'), foreground="red", background="white").place(x=350, y=565)

        print(response_json)
        print(response.status_code)
        if response.status_code == 200:
            Auth.login_success = True
            Auth.full_name = response_json["data"]["full_name"]
            Auth.access_token = response_json["data"]["access_token"]
            self.show_home_screen()
        else:
            tk.Label(self, text="* " + response_json["detail"], font=(Font.main_font, 16, 'bold'), foreground="red", background="white").place(x=350, y=565)
