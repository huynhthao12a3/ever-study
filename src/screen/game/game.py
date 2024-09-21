from src.utils.component import Component
from src.utils.constant import ImageUrl, Api, Auth
from src.utils.file import FileManager
from src.utils.gif import AnimatedGifCanvas
from src.screen.game.flappybird.main import FlappyBird
import tkinter as tk
# Call api, convert json library
import requests
import json

class GameScreen(tk.Frame):
    def __init__(self, master, callback_list, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        self.root = self.winfo_toplevel()  # Get parent window (Tk)
        self.master = master
        self.show_home_screen = callback_list["HomeScreen"]
        self.pygame_window_closed = False

    def load_widgets(self):
        gif_path = ImageUrl.bg_game_screen
        animated_canvas = AnimatedGifCanvas(self, gif_path, self.on_click)
        animated_canvas.pack()

        Component.left_label(self)
        Component.right_button_back(self, self.show_home_screen)

        flappy_bird = tk.Button(self, text="Flappy Bird", font=("Roboto", 20, "bold"), command=self.show_flappy_bird_game)
        flappy_bird.place(x=50, y=50)

    def on_click(self, x, y):
        print(f"Clicked on Page at x={x}, y={y}")

    def show_flappy_bird_game(self):
        self.root.withdraw()  # Hide Tkinter window
        FlappyBird(self.on_flappy_bird_close).run()

    def on_flappy_bird_close(self, game_result= None):
        self.root.deiconify()  # Show Tkinter window
        print("flappy bird closed")
        if game_result is not None:
            print("call api, game_result: ", game_result)
            api_endpoint = Api.api_endpoint + "/ranks/me"
            headers = {
                'Content-Type': 'application/json',
                'Authorization':  "Bearer " + Auth.access_token
            }
            # Call api
            print(api_endpoint, headers)
            response = requests.put(url=api_endpoint, headers=headers, data=json.dumps(game_result))
            response_json = response.json()
            print(response.status_code)
            print(response_json)
