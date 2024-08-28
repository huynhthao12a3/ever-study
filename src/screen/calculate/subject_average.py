from src.utils.component import Component
from src.utils.constant import ImageUrl
from src.utils.file import FileManager
from src.utils.gif import AnimatedGifCanvas
import tkinter as tk


class SubjectAverageScreen(tk.Frame):
    def __init__(self, master, callback_list, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        self.master = master
        self.show_calculate_screen = callback_list["CalculateScreen"]
        self.configure(bg="lightblue")

        self.tx1 = tk.DoubleVar()
        self.tx2 = tk.DoubleVar()
        self.tx3 = tk.DoubleVar()
        self.tx4 = tk.DoubleVar()
        self.gk = tk.DoubleVar()
        self.ck = tk.DoubleVar()

        self.input_tx1 = None
        self.input_tx2 = None
        self.input_tx3 = None
        self.input_tx4 = None
        self.input_gk = None
        self.input_ck = None
        self.label_dtm = None

    def load_widgets(self):
        gif_path = ImageUrl.bg_subject_average
        animated_canvas = AnimatedGifCanvas(self, gif_path, self.on_click)
        animated_canvas.pack()

        Component.left_label(self)
        Component.right_button_back(self, self.show_calculate_screen)

        # Score TX1
        input_tx1 = tk.Entry(self, width=5, font=("Roboto", 16), textvariable=self.tx1, bg="white", validate="key",
                             validatecommand=(self.register(self.validate_float), '%P'))
        input_tx1.place(x=110, y=280)
        input_tx1.bind("<KeyRelease>", self.on_key_release)

        # Score TX2
        input_tx2 = tk.Entry(self, width=5, font=("Roboto", 16), textvariable=self.tx2, bg="white", validate="key",
                             validatecommand=(self.register(self.validate_float), '%P'))
        input_tx2.place(x=196, y=280)
        input_tx2.bind("<KeyRelease>", self.on_key_release)

        # Score TX3
        input_tx3 = tk.Entry(self, width=5, font=("Roboto", 16), textvariable=self.tx3, bg="white", validate="key",
                             validatecommand=(self.register(self.validate_float), '%P'))
        input_tx3.place(x=282, y=280)
        input_tx3.bind("<KeyRelease>", self.on_key_release)

        # Score TX4
        input_tx4 = tk.Entry(self, width=5, font=("Roboto", 16), textvariable=self.tx4, bg="white", validate="key",
                             validatecommand=(self.register(self.validate_float), '%P'))
        input_tx4.place(x=368, y=280)
        input_tx4.bind("<KeyRelease>", self.on_key_release)

        # Score GK
        input_gk = tk.Entry(self, width=5, font=("Roboto", 16), textvariable=self.gk, bg="white", validate="key",
                            validatecommand=(self.register(self.validate_float), '%P'))
        input_gk.place(x=454, y=280)
        input_gk.bind("<KeyRelease>", self.on_key_release)

        # Score CK
        input_ck = tk.Entry(self, width=5, font=("Roboto", 16), textvariable=self.ck, bg="white", validate="key",
                            validatecommand=(self.register(self.validate_float), '%P'))
        input_ck.place(x=540, y=280)
        input_ck.bind("<KeyRelease>", self.on_key_release)

        self.label_dtm = tk.Label(self, width=6, text=str(self.tx1.get()), font=("Roboto", 20, "bold"), bg="white",
                                  fg="red")
        self.label_dtm.place(x=625, y=276)

    def on_click(self, x, y):
        print(f"Clicked on Page at x={x}, y={y}")

    def validate_float(self, input_value):
        try:
            if input_value == "":
                return True
            if len(str(input_value)) > 5: # Limit 5 character
                return False
            float(input_value)
            return True
        except ValueError:
            return False

    def on_key_release(self, event):
        print(self.safe_double_get(self.gk))
        if self.safe_double_get(self.gk) >= 0 and self.safe_double_get(self.ck) >= 0:  # GK and CK already had
            self.label_dtm.config(text=str(self.safe_double_get(self.tx1)))
        else:
            self.label_dtm.config(text=0.0)

    def safe_double_get(self, input_vale):
        try:
            value = input_vale.get()
            if value == "":
                return -1
            return float(value)
        except tk.TclError:
            return -1
