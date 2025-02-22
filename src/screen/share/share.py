﻿import json
from tkinter import messagebox

import requests

from src.utils.component import Component
from src.utils.constant import ImageUrl, Auth, Api, Font, ToolTip
from src.utils.file import FileManager
from src.utils.gif import AnimatedGifCanvas
import tkinter as tk


class ShareScreen(tk.Frame):
    def __init__(self, master, callback_list, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        self.master = master
        self.show_home_screen = callback_list["HomeScreen"]
        self.show_share_list_screen = callback_list["ShareListScreen"]

        # Variable
        self.title = tk.StringVar()
        self.content = tk.StringVar()
        self.title_entry = None
        self.content_text = None

    def load_widgets(self):
        gif_path = ImageUrl.bg_share_screen
        animated_canvas = AnimatedGifCanvas(self, gif_path, self.on_click)
        animated_canvas.pack()

        # Handle change cursor
        animated_canvas.add_clickable_area(400, 525, 525, 550)
        animated_canvas.add_clickable_area(350, 465, 580, 520)

        def limit_character(P):
            if len(P) <= 500:
                return True
            else:
                return False

        custom_font = tk.font.Font(family='Cambria', size=16)
        valid = (self.register(limit_character), '%P')

        Component.left_label(self)
        Component.right_button_back(self, self.show_home_screen)
        Component.right_button_intro(self, ToolTip.share_screen)

        self.title_entry = tk.Entry(self, textvariable=self.title, width=50, borderwidth=3, font=custom_font,
                                    validate="key", validatecommand=valid)
        self.title_entry.place(x=275, y=192, height=40, width=380)

        self.content_text = tk.Text(self, width=50, borderwidth=3, font=custom_font, wrap=tk.WORD)
        self.content_text.place(x=275, y=270, height=180, width=380)

    def on_click(self, x, y):
        print(f"Clicked on Page at x={x}, y={y}")

        title = self.title.get()
        content = self.content_text.get("1.0", tk.END).strip()
        if 400 < x < 525 and 525 < y < 550:
            api_endpoint = Api.api_endpoint + "/shares/me?page_size=10&page=1&sort_by=updated_at&order=desc"
            headers = {
                'Content-Type': 'application/json',
                'Authorization': "Bearer " + Auth.access_token
            }

            try:
                response = requests.get(url=api_endpoint, headers=headers)
                response_json = response.json()

                if response.status_code == 200:
                    Auth.share_list = response_json["data"]
                    print("Auth.share_list: ", Auth.share_list)

            except Exception as e:
                print(e)
                messagebox.showerror("Lỗi mạng", "Vui lòng kểm tra kết nối mạng.")

            self.show_share_list_screen()

        if 350 < x < 580 and 465 < y < 520:
            if (len(title) > 0 and len(content) > 0
                    and Auth.login_success is True):
                print("Send")
                data = {
                    "title": title,
                    "content": content
                }
                api_endpoint = Api.api_endpoint + "/shares"
                headers = {
                    'Content-Type': 'application/json',
                    'Authorization': "Bearer " + Auth.access_token
                }
                # Call api
                try:
                    response = requests.post(url=api_endpoint, headers=headers, data=json.dumps(data))
                    response_json = response.json()

                    print(api_endpoint, headers)
                    print(response.status_code)
                    print(response_json)

                    self.title.set("")
                    self.content_text.delete(1.0, tk.END)

                    if response.status_code == 200:
                        tk.Label(self, text="Gửi thành công", width=16, font=(Font.main_font, 16, 'bold'),
                                 foreground="red", background="white").place(x=350, y=565)
                    else:
                        tk.Label(self, text="Gửi thất bại", width=16, font=(Font.main_font, 16, 'bold'),
                                 foreground="red", background="white").place(x=350, y=565)

                except Exception as e:
                    print(e)
                    tk.Label(self, text="Gửi thất bại", width=16, font=(Font.main_font, 16, 'bold'), foreground="red",
                             background="white").place(x=350, y=565)
            else:
                messagebox.showinfo("Thông báo", "Vui lòng nhập đầy đủ tiêu đề, nội dung.")
