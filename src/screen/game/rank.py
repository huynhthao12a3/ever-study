import json
from tkinter import messagebox
import requests
from src.utils.component import Component
from src.utils.constant import ImageUrl, Auth, Api, Font, Color
from src.utils.gif import AnimatedGifCanvas
import tkinter as tk


class RankScreen(tk.Frame):
    def __init__(self, master, callback_list, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        self.master = master
        self.show_home_screen = callback_list["HomeScreen"]
        self.show_game_mode_screen = callback_list["GameModeScreen"]

        # Định nghĩa các cặp tọa độ cho mỗi top ((x1, x2), (y1, y2))
        self.positions = [
            ((205, 605), (225, 225)),  # Top 1
            ((130, 400), (315, 315)),  # Top 2
            ((530, 790), (315, 315)),  # Top 3
            ((130, 400), (420, 420)),  # Top 4
            ((530, 790), (420, 420))  # Top 5
        ]

    def calculate_center(self, x1, x2, y1, y2):
        center_x = (x1 + x2) // 2
        center_y = (y1 + y2) // 2
        return center_x, center_y

    def load_widgets(self):
        gif_path = ImageUrl.bg_rank_screen
        animated_canvas = AnimatedGifCanvas(self, gif_path, self.on_click)
        animated_canvas.pack()

        Component.left_label(self)
        Component.right_button_back(self, self.show_game_mode_screen)

        api_endpoint = Api.api_endpoint + "/ranks?page_size=5&page=1"
        headers = {
            'Content-Type': 'application/json',
            'Authorization': "Bearer " + Auth.access_token
        }

        try:
            response = requests.get(url=api_endpoint, headers=headers)
            response_json = response.json()

            response_me = requests.get(url=Api.api_endpoint + "/ranks/me", headers=headers)
            response_me_json = response_me.json()
            # print(response_me, response_me_json)
            if response.status_code == 200:
                for i, player in enumerate(response_json["data"][:5]):
                    (x1, x2), (y1, y2) = self.positions[i]
                    center_x, center_y = self.calculate_center(x1, x2, y1, y2)

                    lbl_name = tk.Label(self, text=player["full_name"],
                                        font=(Font.main_font, 30, "bold"),
                                        bg=Color.bg_color_blue, borderwidth=2)
                    lbl_score = tk.Label(self, text=player["game_score"],
                                         font=(Font.main_font, 20, "bold"),
                                         bg=Color.bg_color_blue, fg="red", borderwidth=2)

                    # Đặt vị trí label ở giữa cặp tọa độ
                    lbl_name.place(x=center_x, y=center_y - 25, anchor="center")
                    lbl_score.place(x=center_x, y=center_y + 25, anchor="center")

            if response_me.status_code == 200:
                print("response_me_json:", response_me_json["data"]["game_score"])
                lbl_me = tk.Label(self, text=response_me_json["data"]["game_score"],
                                  font=(Font.main_font, 30, "bold"),
                                  bg=Color.bg_color_yellow, fg="red", borderwidth=2)
                lbl_me.place(x=470, y=485)
            else:
                lbl_me = tk.Label(self, text="0",
                                  font=(Font.main_font, 30, "bold"),
                                  bg=Color.bg_color_yellow, fg="red", borderwidth=2)
                lbl_me.place(x=470, y=485)

        except Exception as e:
            print(e)
            messagebox.showerror("Lỗi mạng", "Vui lòng kểm tra kết nối mạng.")

    def on_click(self, x, y):
        print(f"Clicked on Page at x={x}, y={y}")
