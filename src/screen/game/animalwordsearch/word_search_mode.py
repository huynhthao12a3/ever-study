import json

import requests

from src.screen.game.animalwordsearch.main import AnimalWordSearch
from src.utils.component import Component
from src.utils.constant import ImageUrl, Api, Auth
from src.utils.gif import AnimatedGifCanvas
import tkinter as tk


class WordSearchModeScreen(tk.Frame):
    def __init__(self, master, callback_list, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        self.root = self.winfo_toplevel()  # Get parent window (Tk)
        self.master = master
        self.show_home_screen = callback_list["HomeScreen"]
        self.show_game_mode_screen = callback_list["GameModeScreen"]

    def load_widgets(self):
        gif_path = ImageUrl.bg_word_search_mode_screen
        animated_canvas = AnimatedGifCanvas(self, gif_path, self.on_click)
        animated_canvas.pack()

        Component.left_label(self)
        Component.right_button_back(self, self.show_game_mode_screen)

    def on_click(self, x, y):
        print(f"Clicked on Page at x={x}, y={y}")
        if 55 < x < 135 and 270 < y < 350:
            print("Toán - 1")
            self.animal_word_search_run("math", "lv1")
        if 165 < x < 245 and 270 < y < 350:
            print("Toán - 2")
            self.animal_word_search_run("math", "lv2")
        if 55 < x < 135 and 370 < y < 450:
            print("Toán - 3")
            self.animal_word_search_run("math", "lv3")
        if 165 < x < 245 and 370 < y < 450:
            print("Toán - 4")
            self.animal_word_search_run("math", "lv4")

        if 305 < x < 385 and 270 < y < 350:
            print("Tiếng Anh - 1")
            self.animal_word_search_run("english", "lv1")
        if 415 < x < 495 and 270 < y < 350:
            print("Tiếng Anh - 2")
            self.animal_word_search_run("english", "lv2")
        if 305 < x < 385 and 370 < y < 450:
            print("Tiếng Anh - 3")
            self.animal_word_search_run("english", "lv3")
        if 415 < x < 495 and 370 < y < 450:
            print("Tiếng Anh - 4")
            self.animal_word_search_run("english", "lv4")

        if 555 < x < 635 and 270 < y < 350:
            print("LS-DL - 1")
            self.animal_word_search_run("history", "lv1")
        if 665 < x < 745 and 270 < y < 350:
            print("LS-DL - 2")
            self.animal_word_search_run("history", "lv2")
        if 555 < x < 635 and 370 < y < 450:
            print("LS-DL - 3")
            self.animal_word_search_run("history", "lv3")
        if 665 < x < 745 and 370 < y < 450:
            print("LS-DL - 4")
            self.animal_word_search_run("history", "lv4")

    def animal_word_search_run(self, selected_subject, selected_level):
        self.root.withdraw()  # Hide Tkinter window
        AnimalWordSearch(self.on_animal_word_search_close, selected_subject, selected_level).run()

    def on_animal_word_search_close(self, game_result=None):
        self.root.deiconify()  # Show Tkinter window
        print("Animal Word Search closed")
        print(game_result)
        if game_result is not None and Auth.login_success is True:
            print("call api, game_result: ", game_result)
            api_endpoint = Api.api_endpoint + "/ranks/me"
            headers = {
                'Content-Type': 'application/json',
                'Authorization': "Bearer " + Auth.access_token
            }
            # Call api
            response = requests.put(url=api_endpoint, headers=headers, data=json.dumps(game_result))
            response_json = response.json()

            print(api_endpoint, headers)
            print(response.status_code)
            print(response_json)
