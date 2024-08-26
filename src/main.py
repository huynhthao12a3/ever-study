import tkinter as tk
from PIL import Image, ImageTk

from src.screen.author import AuthorScreen
from src.screen.calculate import CalculateScreen
from src.screen.game import GameScreen
from src.screen.home import HomeScreen
from src.screen.learn import LearnScreen
from src.screen.other import OtherScreen


class EverStudy(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("Ever Study")
        self.geometry("800x600")
        self.resizable(False, False)

        self.container = tk.Frame(self, bg="lightblue")
        self.container.pack(fill="both", expand=True)

        self.pages = {}
        self.load_pages()
        self.current_page = None
        self.show_page("HomeScreen")

    def load_pages(self):
        # Routing
        home_callback_list = {
            "LearnScreen": self.show_learn_screen,
            "AuthorScreen": self.show_author_screen,
            "GameScreen": self.show_game_screen
        }
        learn_callback_list = {
            "HomeScreen": self.show_home_screen
        }
        author_callback_list = {
            "HomeScreen": self.show_home_screen
        }
        calculate_callback_list = {
            "HomeScreen": self.show_home_screen
        }
        game_callback_list = {
            "HomeScreen": self.show_home_screen
        }
        other_callback_list = {
            "HomeScreen": self.show_home_screen
        }

        self.pages["HomeScreen"] = HomeScreen(self.container, home_callback_list)
        self.pages["LearnScreen"] = LearnScreen(self.container, learn_callback_list)
        self.pages["AuthorScreen"] = AuthorScreen(self.container, author_callback_list)
        self.pages["CalculateScreen"] = CalculateScreen(self.container, calculate_callback_list)
        self.pages["GameScreen"] = GameScreen(self.container, game_callback_list)
        self.pages["OtherScreen"] = OtherScreen(self.container, other_callback_list)

    def show_page(self, page_name):
        if self.current_page:
            self.current_page.pack_forget()

        page = self.pages.get(page_name)
        if page:
            page.pack(fill="both", expand=True)
            self.current_page = page

    def show_home_screen(self):
        self.show_page("HomeScreen")

    def show_learn_screen(self):
        self.show_page("LearnScreen")

    def show_author_screen(self):
        self.show_page("AuthorScreen")

    def show_calculate_screen(self):
        self.show_page("CalculateScreen")

    def show_game_screen(self):
        self.show_page("GameScreen")

    def show_other_screen(self):
        self.show_page("OtherScreen")

    # def on_click(event):
    #     x = event.x
    #     y = event.y
    #     print(f"Clicked at x={x}, y={y}")
