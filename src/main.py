import tkinter as tk

from src.screen.author.author import AuthorScreen
from src.screen.calculate.academic_result import AcademicResultScreen
from src.screen.calculate.calculate import CalculateScreen
from src.screen.calculate.subject_average import SubjectAverageScreen
from src.screen.game.game_mode import GameModeScreen
from src.screen.game.normal_game_mode import NormalGameModeScreen
from src.screen.game.rank import RankScreen
from src.screen.utility.exam import ExamScreen
from src.screen.utility.exams.traffic_safety import TrafficSafetyScreen
from src.screen.utility.time_table import TimeTableScreen
from src.screen.utility.utility import UtilityScreen
from src.screen.game.game import GameScreen
from src.screen.home import HomeScreen
from src.screen.learn.learn import LearnScreen
from src.screen.learn.math import MathScreen
from src.screen.login.login import LoginScreen
from src.screen.other.other import OtherScreen
from src.screen.share.share import ShareScreen
from src.utils.constant import ImageUrl
from src.utils.file import FileManager


class EverStudy(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("Ever Study")
        self.iconbitmap(FileManager().resource_path(ImageUrl.app_icon))
        print(FileManager().resource_path(ImageUrl.app_icon))
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
            "UtilityScreen": self.show_utility_screen,
            "ShareScreen": self.show_share_screen,
            "OtherScreen": self.show_other_screen,
            "AuthorScreen": self.show_author_screen,
            "LoginScreen": self.show_login_screen
        }
        learn_callback_list = {
            "HomeScreen": self.show_home_screen,
            "LearnScreen": self.show_learn_screen,
            "MathScreen": self.show_math_screen
        }
        author_callback_list = {
            "HomeScreen": self.show_home_screen
        }
        calculate_callback_list = {
            "UtilityScreen": self.show_utility_screen,
            "CalculateScreen": self.show_calculate_screen,
            "SubjectAverageScreen": self.show_subject_average_screen,
            "AcademicResultScreen": self.show_academic_result_screen,
        }
        game_callback_list = {
            "HomeScreen": self.show_home_screen,
            "GameScreen": self.show_game_screen,
            "GameModeScreen": self.show_game_mode_screen,
            "NormalGameModeScreen": self.show_normal_game_mode_screen,
            "RankScreen": self.show_rank_screen
        }
        other_callback_list = {
            "HomeScreen": self.show_home_screen
        }
        share_callback_list = {
            "HomeScreen": self.show_home_screen
        }
        utility_callback_list = {
            "HomeScreen": self.show_home_screen,
            "CalculateScreen": self.show_calculate_screen,
            "SubjectAverageScreen": self.show_subject_average_screen,
            "AcademicResultScreen": self.show_academic_result_screen,
            "UtilityScreen": self.show_utility_screen,
            "TimeTableScreen": self.show_time_table_screen,
            "ExamScreen": self.show_exam_screen,
            "TrafficSafetyScreen": self.show_traffic_safety_screen
        }
        login_callback_list = {
            "HomeScreen": self.show_home_screen
        }

        self.screens["HomeScreen"] = HomeScreen(self.container, home_callback_list)
        self.screens["LearnScreen"] = LearnScreen(self.container, learn_callback_list)
        self.screens["MathScreen"] = MathScreen(self.container, learn_callback_list)
        self.screens["AuthorScreen"] = AuthorScreen(self.container, author_callback_list)
        self.screens["CalculateScreen"] = CalculateScreen(self.container, calculate_callback_list)
        self.screens["SubjectAverageScreen"] = SubjectAverageScreen(self.container, calculate_callback_list)
        self.screens["AcademicResultScreen"] = AcademicResultScreen(self.container, calculate_callback_list)
        self.screens["GameScreen"] = GameScreen(self.container, game_callback_list)
        self.screens["GameModeScreen"] = GameModeScreen(self.container, game_callback_list)
        self.screens["NormalGameModeScreen"] = NormalGameModeScreen(self.container, game_callback_list)
        self.screens["RankScreen"] = RankScreen(self.container, game_callback_list)
        self.screens["OtherScreen"] = OtherScreen(self.container, other_callback_list)
        self.screens["ShareScreen"] = ShareScreen(self.container, share_callback_list)
        self.screens["UtilityScreen"] = UtilityScreen(self.container, utility_callback_list)
        self.screens["TimeTableScreen"] = TimeTableScreen(self.container, utility_callback_list)
        self.screens["ExamScreen"] = ExamScreen(self.container, utility_callback_list)
        self.screens["TrafficSafetyScreen"] = TrafficSafetyScreen(self.container, utility_callback_list)
        self.screens["LoginScreen"] = LoginScreen(self.container, login_callback_list)

    def show_screen(self, screen_name):
        print("screen_name: ", screen_name)
        print("current_screen: ", self.current_screen)
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

    def show_math_screen(self):
        self.show_screen("MathScreen")

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

    def show_game_mode_screen(self):
        self.show_screen("GameModeScreen")

    def show_normal_game_mode_screen(self):
        self.show_screen("NormalGameModeScreen")

    def show_rank_screen(self):
        self.show_screen("RankScreen")

    def show_other_screen(self):
        self.show_screen("OtherScreen")

    def show_share_screen(self):
        self.show_screen("ShareScreen")

    def show_utility_screen(self):
        self.show_screen("UtilityScreen")

    def show_time_table_screen(self):
        self.show_screen("TimeTableScreen")

    def show_exam_screen(self):
        self.show_screen("ExamScreen")

    def show_traffic_safety_screen(self):
        self.show_screen("TrafficSafetyScreen")

    def show_login_screen(self):
        self.show_screen("LoginScreen")
