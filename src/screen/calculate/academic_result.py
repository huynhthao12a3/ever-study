import tkinter as tk

from src.utils.component import Component
from src.utils.constant import ImageUrl, Color, Font
from src.utils.gif import AnimatedGifCanvas


class AcademicResultScreen(tk.Frame):
    def __init__(self, master, callback_list, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        self.master = master
        self.show_calculate_screen = callback_list["CalculateScreen"]

        self.mathematics = tk.DoubleVar()
        self.literature = tk.DoubleVar()
        self.english = tk.DoubleVar()
        self.natural_sciences = tk.DoubleVar()
        self.history_geography = tk.DoubleVar()
        self.computer_science = tk.DoubleVar()
        self.civic_education = tk.DoubleVar()
        self.technology = tk.DoubleVar()
        self.result = ""

        self.input_mathematics = None
        self.input_literature = None
        self.input_english = None
        self.input_natural_sciences = None
        self.input_history_geography = None
        self.input_computer_science = None
        self.input_civic_education = None
        self.input_technology = None
        self.label_result = None

    def load_widgets(self):
        gif_path = ImageUrl.bg_academic_result
        animated_canvas = AnimatedGifCanvas(self, gif_path, self.on_click)
        animated_canvas.pack()

        Component.left_label(self)
        Component.right_button_back(self, self.show_calculate_screen)

        # Score Mathematics
        self.input_mathematics = tk.Entry(self, width=5, font=(Font.main_font, 18), textvariable=self.mathematics, bg="white",
                                          validate="key",
                                          validatecommand=(self.register(self.validate_float), '%P'))
        self.input_mathematics.place(x=66, y=305)
        self.input_mathematics.bind("<KeyRelease>", self.on_key_release)

        # Score Literature
        self.input_literature = tk.Entry(self, width=5, font=(Font.main_font, 18), textvariable=self.literature, bg="white",
                                         validate="key",
                                         validatecommand=(self.register(self.validate_float), '%P'))
        self.input_literature.place(x=145, y=305)
        self.input_literature.bind("<KeyRelease>", self.on_key_release)

        # Score English
        self.input_english = tk.Entry(self, width=5, font=(Font.main_font, 18), textvariable=self.english, bg="white",
                                      validate="key",
                                      validatecommand=(self.register(self.validate_float), '%P'))
        self.input_english.place(x=230, y=305)
        self.input_english.bind("<KeyRelease>", self.on_key_release)

        # Score Natural Sciences
        self.input_natural_sciences = tk.Entry(self, width=5, font=(Font.main_font, 18), textvariable=self.natural_sciences,
                                               bg="white", validate="key",
                                               validatecommand=(self.register(self.validate_float), '%P'))
        self.input_natural_sciences.place(x=318, y=305)
        self.input_natural_sciences.bind("<KeyRelease>", self.on_key_release)

        # Score History and Geography
        self.input_history_geography = tk.Entry(self, width=5, font=(Font.main_font, 18), textvariable=self.history_geography,
                                                bg="white", validate="key",
                                                validatecommand=(self.register(self.validate_float), '%P'))
        self.input_history_geography.place(x=400, y=305)
        self.input_history_geography.bind("<KeyRelease>", self.on_key_release)

        # Score Computer Science
        self.input_computer_science = tk.Entry(self, width=5, font=(Font.main_font, 18), textvariable=self.computer_science,
                                               bg="white", validate="key",
                                               validatecommand=(self.register(self.validate_float), '%P'))
        self.input_computer_science.place(x=490, y=305)
        self.input_computer_science.bind("<KeyRelease>", self.on_key_release)

        # Score Civic Education
        self.input_civic_education = tk.Entry(self, width=5, font=(Font.main_font, 18), textvariable=self.civic_education,
                                              bg="white", validate="key",
                                              validatecommand=(self.register(self.validate_float), '%P'))
        self.input_civic_education.place(x=580, y=305)
        self.input_civic_education.bind("<KeyRelease>", self.on_key_release)

        # Score Technology
        self.input_technology = tk.Entry(self, width=5, font=(Font.main_font, 18), textvariable=self.technology, bg="white",
                                         validate="key",
                                         validatecommand=(self.register(self.validate_float), '%P'))
        self.input_technology.place(x=674, y=305)
        self.input_technology.bind("<KeyRelease>", self.on_key_release)

        # Show result
        self.label_result = tk.Label(self, width=8, text=str(self.result), font=(Font.main_font, 20, "bold"), bg=Color.bg_main,
                                     fg=Color.text_color_red)
        self.label_result.place(x=455, y=465)

    def on_click(self, x, y):
        print(f"Clicked on Page at x={x}, y={y}")

    def validate_float(self, input_value):
        try:
            if input_value == "":
                return True
            if len(str(input_value)) > 5:  # Limit 5 character
                return False
            float(input_value)
            return True
        except ValueError:
            return False

    def on_key_release(self, event):
        score_list = [self.safe_double_get(self.mathematics), self.safe_double_get(self.literature),
                      self.safe_double_get(self.english), self.safe_double_get(self.natural_sciences),
                      self.safe_double_get(self.history_geography), self.safe_double_get(self.computer_science),
                      self.safe_double_get(self.civic_education), self.safe_double_get(self.technology)]

        count_above_8 = sum(score >= 8.0 for score in score_list)
        count_above_6_5 = sum(score >= 6.5 for score in score_list)
        count_above_5 = sum(score >= 5.0 for score in score_list)

        if all(score >= 6.5 for score in score_list) and count_above_8 >= 6:
            self.result = "Tốt"
        elif all(score >= 5.0 for score in score_list) and count_above_6_5 >= 6:
            self.result = "Khá"
        elif all(score >= 3.5 for score in score_list) and count_above_5 >= 6:
            self.result = "Đạt"
        else:
            self.result = "Chưa đạt"

        self.label_result.config(text=self.result)

    def safe_double_get(self, input_vale):
        try:
            value = input_vale.get()
            if value == "":
                return -1
            return float(value)
        except tk.TclError:
            return -1
