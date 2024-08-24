import tkinter as tk
from tkinter import font
import pygame.display

from src.utils.constant import Auth, Api
# from tkextrafont import Font
from src.utils.file import FileManager
# Call api, convert json library
import requests
import json

from src.utils.popup import ErasablePopup


class Login:
    def __init__(self, main_instance):
        if Auth.login_success is True:
            print(Auth.full_name, "already login")
        else:
            if len(main_instance.popups) > 0:
                main_instance.popups[0].un_draw(main_instance.screen)
                main_instance.popups[1].un_draw(main_instance.screen)
                pygame.draw.rect(main_instance.screen, (255, 255, 255), pygame.Rect(710, 4, 88, 30 ), 2, 10)

            # screen.blit(pygame.transform.scale(FileManager().load_image("image/background/tick-success.png", True), (10, 10)),(0,0))
            self.root = tk.Tk()
            self.root.geometry('400x300')
            self.root.title('Đăng nhập')
            self.root.resizable(False, False)

            # App config
            self.icon = tk.PhotoImage(file=FileManager().resource_path("image/setting/apple.png"))
            # self.background = tk.PhotoImage(file=FileManager().resource_path("image/setting/khoidau.png"))
            self.root.iconphoto(False, self.icon)
            # self.place = tk.Label(self.root, image=self.background)
            # self.place.place(x=0, y=0)

            self.root.wm_attributes("-transparent", "aqua")

            # Variable
            self.username_verify = tk.StringVar()
            self.password_verify = tk.StringVar()
            self.username_login_entry = None
            self.password_login_entry = None
            self.login_success_screen = None

            # font_large = Font(file=FileManager().resource_path("font/Roboto-Black.ttf"), family="Roboto", size=20)
            self.font_small = pygame.font.SysFont('roboto', 20)

            # tk.Label(self.root, text="-*- Chào mừng bạn đến với Ever Study -*-", bg="aqua").pack()
            # tk.Label(self.root, text="", height=5).pack()
            tk.Label(self.root, text="Vui lòng nhập thông tin tài khoản", font=('Roboto', 18, 'bold')).pack()
            tk.Label(self.root, text="").pack()

            tk.Label(self.root, text="Tài khoản", font=('Roboto', 14)).pack()
            username_login_entry = tk.Entry(self.root, textvariable=self.username_verify, width=50, borderwidth=3)
            username_login_entry.pack()

            tk.Label(self.root, text="", height=1).pack()

            tk.Label(self.root, text="Mật khẩu", font=('Roboto', 14)).pack()
            password_login_entry = tk.Entry(self.root, textvariable=self.password_verify, show='*', width=50, borderwidth=3)
            password_login_entry.pack()

            tk.Label(self.root, text="").pack()
            tk.Button(self.root, text="Đăng nhập", width=20, height=2, command=lambda: self.login_verify(main_instance), borderwidth=2, cursor="circle").pack()

            # tk.Button(self.root, text="delete", width=20, height=2, command=self.login_success_screen.destroy(), borderwidth=2,
            #           cursor="circle").pack()

            self.root.mainloop()

    # Implementing event on login button

    def login_verify(self, main_instance):
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
            tk.Label(self.root, text="Đăng nhập thất bại", width=16, font=('Roboto', 16, 'bold'), foreground="red").place(x=0, y=270)

        print(response_json)
        print(response.status_code)
        if response.status_code == 200:
            # self.get_info(main_instance, response_json["data"]["access_token"])
            Auth.login_success = True
            Auth.full_name = response_json["data"]["full_name"]
            main_instance.popups[0] = (ErasablePopup(pygame.font.SysFont("roboto", 14), "✮ Hi, " + Auth.full_name))
            main_instance.popups[1] = (ErasablePopup(pygame.font.SysFont("roboto", 14), ""))
            self.root.destroy()
        else:
            tk.Label(self.root, text="* " + response_json["detail"], font=('Roboto', 12), foreground="red").place(x=0, y=270)

    def get_info(self, main_instance, access_token):
        api_endpoint = Api.api_endpoint + "/users/me"
        headers = {
            'Content-Type': 'application/json',
            'Authorization':  "Bearer " + access_token
        }
        # Call api
        response = requests.get(url=api_endpoint, headers=headers)
        response_json = response.json()
        print(response.status_code)
        print(response_json)
        if response.status_code == 200:
            Auth.login_success = True
            Auth.full_name = response_json["data"]["full_name"]
            main_instance.popups[0] = (ErasablePopup(pygame.font.SysFont("roboto", 14), "✮ Hi, " + Auth.full_name))
            main_instance.popups[1] = (ErasablePopup(pygame.font.SysFont("roboto", 14), ""))
            self.root.destroy()

    def login_success(self):
        # global login_success_screen
        self.login_success_screen = tk.Toplevel(self.root)
        self.login_success_screen.title("Success")
        self.login_success_screen.geometry("150x100")
        tk.Label(self.login_success_screen, text="Login Success").pack()
