import tkinter as tk
from tkextrafont import Font
from src.utils.file import FileManager
# Call api, convert json library
import requests
import json


class Login:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry('800x600')
        self.root.title('Ever Study')
        self.root.resizable(False, False)

        # App config
        self.icon = tk.PhotoImage(file=FileManager().resource_path("image/setting/apple.png"))
        self.backgound = tk.PhotoImage(file=FileManager().resource_path("image/setting/khoidau.png"))
        self.root.iconphoto(False, self.icon)
        self.place = tk.Label(self.root, image=self.backgound)
        self.place.place(x=0, y=0)

        self.root.wm_attributes("-transparent", "aqua")

        # Variable
        self.username_verify = tk.StringVar()
        self.password_verify = tk.StringVar()
        self.username_login_entry = None
        self.password_login_entry = None

        font_large = Font(file=FileManager().resource_path("font/Roboto-Black.ttf"), family="Roboto", size=20)
        font_small = Font(file=FileManager().resource_path("font/Roboto-Thin.ttf"), family="Roboto", size=12)

        tk.Label(self.root, text="-*- Chào mừng bạn đến với Ever Study -*-", font=font_large, bg="aqua").pack()
        tk.Label(self.root, text="", height=5).pack()
        tk.Label(self.root, text="Vui lòng nhập thông tin tài khoản", font=font_large).pack()
        tk.Label(self.root, text="").pack()

        tk.Label(self.root, text="Tài khoản * ", font=font_small).pack()
        username_login_entry = tk.Entry(self.root, textvariable=self.username_verify, width=50, borderwidth=3,
                                        font=font_small)
        username_login_entry.pack()

        tk.Label(self.root, text="").pack()
        tk.Label(self.root, text="Mật khẩu * ", font=font_small).pack()
        password_login_entry = tk.Entry(self.root, textvariable=self.username_verify, show='*', width=50, borderwidth=3,
                                        font=font_small)
        password_login_entry.pack()

        tk.Label(self.root, text="").pack()
        tk.Button(self.root, text="Đăng nhập", width=20, height=2, command=self.login_verify, borderwidth=2,
                  cursor="circle").pack()

        self.root.mainloop()

    # Implementing event on login button

    def login_verify(self):
        username1 = self.username_verify.get()
        password1 = self.password_verify.get()
        # username_login_entry.delete(0, END)
        # password_login_entry.delete(0, END)

        # defining the api-endpoint
        API_ENDPOINT = "https://backend-34tq.onrender.com/login"

        # data to be sent to api
        data = {
            "username": "huynhthao@gmail.com",
            "password": "123456"
        }
        headers = {'Content-Type': 'application/json'}

        # sending post request and saving response as response object
        r = requests.post(url=API_ENDPOINT, json=data, headers=headers)

        # extracting response text
        pastebin_url = r.text
        test = json.loads(pastebin_url)
        # print("The pastebin URL is:%s" % pastebin_url)
        print(r.status_code)
        print(r.json()["data"])
        # print(test["data"])

        if r.status_code == 200:
            self.login_sucess()

    # Designing popup for login success

    def login_sucess(self):
        global login_success_screen
        self.root = tk.Toplevel(self.root)
        self.root.title("Success")
        self.root.geometry("150x100")
        tk.Label(self.root, text="Login Success").pack()
