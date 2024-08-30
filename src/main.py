import tkinter as tk

from src.screen.author.author import AuthorScreen
from src.screen.calculate.academic_result import AcademicResultScreen
from src.screen.calculate.calculate import CalculateScreen
from src.screen.calculate.subject_average import SubjectAverageScreen
from src.screen.discovery.discovery import DiscoveryScreen
from src.screen.game.game import GameScreen
from src.screen.home import HomeScreen
from src.screen.learn.learn import LearnScreen
from src.screen.login.login import LoginScreen
from src.screen.other.other import OtherScreen
from src.screen.share.share import ShareScreen


class EverStudy(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("Ever Study")
        self.geometry("800x600")
        self.resizable(False, False)

        self.container = tk.Frame(self, bg="lightblue")
        self.container.pack(fill="both", expand=True)

        self.screens = {}
        self.load_screens()
        self.current_screen = None
        self.show_screen("HomeScreen")

    def load_screens(self):
        # Routing
        home_callback_list = {
            "LearnScreen": self.show_learn_screen,
            "CalculateScreen": self.show_calculate_screen,
            "GameScreen": self.show_game_screen,
            "DiscoveryScreen": self.show_discovery_screen,
            "ShareScreen": self.show_share_screen,
            "OtherScreen": self.show_other_screen,
            "AuthorScreen": self.show_author_screen,
            "LoginScreen": self.show_login_screen
        }
        learn_callback_list = {
            "HomeScreen": self.show_home_screen
        }
        author_callback_list = {
            "HomeScreen": self.show_home_screen
        }
        calculate_callback_list = {
            "HomeScreen": self.show_home_screen,
            "SubjectAverageScreen": self.show_subject_average_screen,
            "AcademicResultScreen": self.show_academic_result_screen,
        }
        subject_average_callback_list = {
            "CalculateScreen": self.show_calculate_screen
        }
        game_callback_list = {
            "HomeScreen": self.show_home_screen
        }
        other_callback_list = {
            "HomeScreen": self.show_home_screen
        }
        share_callback_list = {
            "HomeScreen": self.show_home_screen
        }
        discovery_callback_list = {
            "HomeScreen": self.show_home_screen
        }
        login_callback_list = {
            "HomeScreen": self.show_home_screen
        }

        self.screens["HomeScreen"] = HomeScreen(self.container, home_callback_list)
        self.screens["LearnScreen"] = LearnScreen(self.container, learn_callback_list)
        self.screens["AuthorScreen"] = AuthorScreen(self.container, author_callback_list)
        self.screens["CalculateScreen"] = CalculateScreen(self.container, calculate_callback_list)
        self.screens["SubjectAverageScreen"] = SubjectAverageScreen(self.container, subject_average_callback_list)
        self.screens["AcademicResultScreen"] = AcademicResultScreen(self.container, subject_average_callback_list)
        self.screens["GameScreen"] = GameScreen(self.container, game_callback_list)
        self.screens["OtherScreen"] = OtherScreen(self.container, other_callback_list)
        self.screens["ShareScreen"] = ShareScreen(self.container, share_callback_list)
        self.screens["DiscoveryScreen"] = DiscoveryScreen(self.container, discovery_callback_list)
        self.screens["LoginScreen"] = LoginScreen(self.container, login_callback_list)

    def show_screen(self, screen_name):
        print(screen_name)
        print(self.current_screen)
        if self.current_screen:
            # Hide current screen and destroy all screen's widgets
            self.current_screen.pack_forget()
            # self.current_screen.clear_widgets()
            for widget in self.current_screen.winfo_children():
                widget.destroy()
            self.current_screen.update_idletasks()

        new_screen = self.screens.get(screen_name)  # Init Screen
        new_screen.load_widgets()  # Load all widgets: GIF, Button, Label
        if new_screen:
            new_screen.pack(fill="both", expand=True)
            self.current_screen = new_screen

    def show_home_screen(self):
        self.show_screen("HomeScreen")

    def show_learn_screen(self):
        self.show_screen("LearnScreen")

    def show_author_screen(self):
        self.show_screen("AuthorScreen")

    def show_calculate_screen(self):
        self.show_screen("CalculateScreen")

    def show_subject_average_screen(self):
        self.show_screen("SubjectAverageScreen")

    def show_academic_result_screen(self):
        self.show_screen("AcademicResultScreen")

    def show_game_screen(self):
        self.show_screen("GameScreen")

    def show_other_screen(self):
        self.show_screen("OtherScreen")

    def show_share_screen(self):
        self.show_screen("ShareScreen")

    def show_discovery_screen(self):
        self.show_screen("DiscoveryScreen")

    def show_login_screen(self):
        self.show_screen("LoginScreen")