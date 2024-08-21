import tkinter as tk

import pygame.display

from src.utils.constant import Auth
# from tkextrafont import Font
from src.utils.file import FileManager
# Call api, convert json library
import requests
import json


class Login:
    def __init__(self, screen, popups, erasable_popup):
        if len(Auth.full_name) > 0:
            print(Auth.full_name, "already login")
        else:
            Auth.full_name = "Huỳnh Văn Thảo"
            Auth.login_success = True
            if len(popups) > 0:
                popups[0].un_draw(screen)
                popups[1].un_draw(screen)
                pygame.draw.rect(screen, (255,255,255), pygame.Rect(710, 4, 88, 30 ), 2, 10)
            popups[0] = (erasable_popup(pygame.font.SysFont("roboto", 14), "✮ Hi, " + Auth.full_name))
            popups[1] = (erasable_popup(pygame.font.SysFont("roboto", 14), ""))
            # screen.blit(pygame.transform.scale(FileManager().load_image("image/background/tick-success.png", True), (10, 10)),(0,0))
            self.root = tk.Tk()
            self.root.geometry('800x600')
            self.root.title('Ever Study')
            self.root.resizable(False, False)

            # App config
            self.icon = tk.PhotoImage(file=FileManager().resource_path("image/setting/apple.png"))
            self.background = tk.PhotoImage(file=FileManager().resource_path("image/setting/khoidau.png"))
            self.root.iconphoto(False, self.icon)
            self.place = tk.Label(self.root, image=self.background)
            self.place.place(x=0, y=0)

            self.root.wm_attributes("-transparent", "aqua")

            # Variable
            self.username_verify = tk.StringVar()
            self.password_verify = tk.StringVar()
            self.username_login_entry = None
            self.password_login_entry = None
            self.login_success_screen = None

            # font_large = Font(file=FileManager().resource_path("font/Roboto-Black.ttf"), family="Roboto", size=20)
            # font_small = Font(file=FileManager().resource_path("font/Roboto-Thin.ttf"), family="Roboto", size=12)

            tk.Label(self.root, text="-*- Chào mừng bạn đến với Ever Study -*-", bg="aqua").pack()
            tk.Label(self.root, text="", height=5).pack()
            tk.Label(self.root, text="Vui lòng nhập thông tin tài khoản").pack()
            tk.Label(self.root, text="").pack()

            tk.Label(self.root, text="Tài khoản * ").pack()
            username_login_entry = tk.Entry(self.root, textvariable=self.username_verify, width=50, borderwidth=3
                                            )
            username_login_entry.pack()

            tk.Label(self.root, text="", height=2).pack()

            tk.Label(self.root, text="Mật khẩu * ").pack()
            password_login_entry = tk.Entry(self.root, textvariable=self.password_verify, show='*', width=50,
                                            borderwidth=3
                                            )
            password_login_entry.pack()

            tk.Label(self.root, text="").pack()
            tk.Button(self.root, text="Đăng nhập", width=20, height=2, command=self.login_verify, borderwidth=2,
                      cursor="circle").pack()

            # tk.Button(self.root, text="delete", width=20, height=2, command=self.login_success_screen.destroy(), borderwidth=2,
            #           cursor="circle").pack()

            self.root.mainloop()

    # Implementing event on login button

    def login_verify(self):
        username = self.username_verify.get()
        password = self.password_verify.get()

        # defining the api-endpoint
        api_endpoint = "https://backend-34tq.onrender.com/login"
        headers = {'Content-Type': 'application/json'}
        data = {
            "username": username,  #"huynhthao@gmail.com",
            "password": password  #"123456"
        }

        # cal api
        response = requests.post(url=api_endpoint, json=data, headers=headers)

        # extracting response text
        pastebin_url = response.text
        test = json.loads(pastebin_url)
        # print("The pastebin URL is:%s" % pastebin_url)
        print(response.status_code)
        print(response.json()["data"])
        # print(test["data"])

        if response.status_code == 200:
            self.root.destroy()

    # Designing popup for login success

    def login_success(self):
        # global login_success_screen
        self.login_success_screen = tk.Toplevel(self.root)
        self.login_success_screen.title("Success")
        self.login_success_screen.geometry("150x100")
        tk.Label(self.login_success_screen, text="Login Success").pack()
