from src.screen.game.applecatcher.main import AppleCatcher
from src.utils.component import Component
from src.utils.constant import ImageUrl, Api, Auth, Font, GameSetting
from src.utils.file import FileManager
from src.utils.gif import AnimatedGifCanvas
from src.screen.game.flappybird.main import FlappyBird
from src.screen.game.animalwordsearch.main import AnimalWordSearch
import tkinter as tk
# Call api, convert json library
import requests
import json


class GameModeScreen(tk.Frame):
    def __init__(self, master, callback_list, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        self.root = self.winfo_toplevel()  # Get parent window (Tk)
        self.master = master
        self.show_home_screen = callback_list["HomeScreen"]
        self.show_game_screen = callback_list["GameScreen"]
        self.show_normal_game_mode_screen = callback_list["NormalGameModeScreen"]
        self.show_rank_screen = callback_list["RankScreen"]
        self.show_word_search_mode_screen = callback_list["WordSearchModeScreen"]
        self.pygame_window_closed = False

    def load_widgets(self):
        gif_path = ImageUrl.bg_game_mode_screen
        animated_canvas = AnimatedGifCanvas(self, gif_path, self.on_click)
        animated_canvas.pack()

        Component.left_label(self)
        Component.right_button_back(self, self.show_game_screen)

    def on_click(self, x, y):
        print(f"Clicked on Page at x={x}, y={y}")
        if 145 < x < 320 and 200 < y < 400:
            print("Normal game mode")
            GameSetting.selected_game_mode = "Normal"
            self.show_normal_game_mode_screen()
        if 465 < x < 665 and 205 < y < 400:
            print("Rank game mode")
            GameSetting.selected_game_mode = "Rank"
            if GameSetting.selected_game == "Flappy_Bird":
                self.flappy_bird_run("all")
            if GameSetting.selected_game == "Apple_Catcher":
                self.apple_catcher_run("all")
            if GameSetting.selected_game == "Word_Search":
                self.show_word_search_mode_screen()
                # self.animal_word_search_run()

        if 90 < x < 210 and 420 < y < 580:
            print("BXH")
            self.show_rank_screen()

    def flappy_bird_run(self, selected_subject):
        self.root.withdraw()  # Hide Tkinter window
        FlappyBird(self.on_flappy_bird_close, selected_subject).run()

    def apple_catcher_run(self, selected_subject):
        self.root.withdraw()  # Hide Tkinter window
        AppleCatcher(self.on_apple_catcher_close, selected_subject).run()

    def on_flappy_bird_close(self, game_result=None):
        self.root.deiconify()  # Show Tkinter window
        print("flappy bird closed")
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

    def on_apple_catcher_close(self, game_result=None):
        self.root.deiconify()  # Show Tkinter window
        print("Apple Catcher closed")
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


