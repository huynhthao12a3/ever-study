import json

import requests

from src.utils.component import Component
from src.utils.constant import ImageUrl, Auth, Api, Font
from src.utils.file import FileManager
from src.utils.gif import AnimatedGifCanvas
import tkinter as tk


class ShareScreen(tk.Frame):
    def __init__(self, master, callback_list, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        self.master = master
        self.show_home_screen = callback_list["HomeScreen"]

        # Variable
        self.title = tk.StringVar()
        self.content = tk.StringVar()
        self.title_entry = None
        self.content_text = None

    def load_widgets(self):
        gif_path = ImageUrl.bg_share_screen
        animated_canvas = AnimatedGifCanvas(self, gif_path, self.on_click)
        animated_canvas.pack()

        def limit_character(P):
            if len(P) <= 500:
                return True
            else:
                return False

        custom_font = tk.font.Font(family='Cambria', size=16)
        valid = (self.register(limit_character), '%P')

        Component.left_label(self)
        Component.right_button_back(self, self.show_home_screen)

        self.title_entry = tk.Entry(self, textvariable=self.title, width=50, borderwidth=3, font=custom_font, validate="key", validatecommand=valid)
        self.title_entry.place(x=275, y=192, height=40, width=380)

        self.content_text = tk.Text(self, width=50, borderwidth=3, font=custom_font, wrap=tk.WORD)
        self.content_text.place(x=275, y=270, height=180, width=380)


    def on_click(self, x, y):
        print(f"Clicked on Page at x={x}, y={y}")
        title = self.title.get()
        content = self.content_text.get("1.0", tk.END).strip()
        if (375 < x < 575 and 480 < y < 530
                and len(title) > 0 and len(content) > 0
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
                    tk.Label(self, text="Gửi thành công", width=16, font=(Font.main_font, 16, 'bold'), foreground="red", background="white").place(x=350, y=565)
                else:
                    tk.Label(self, text="Gửi thất bại", width=16, font=(Font.main_font, 16, 'bold'), foreground="red", background="white").place(x=350, y=565)

            except Exception as e:
                print(e)
                tk.Label(self, text="Gửi thất bại", width=16, font=(Font.main_font, 16, 'bold'), foreground="red", background="white").place(x=350, y=565)
