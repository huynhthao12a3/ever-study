import tkinter as tk
from PIL import Image, ImageTk

from src.utils.constant import Color, Font
from src.utils.file import FileManager

class Tooltip:
    def __init__(self, widget, text, app_width=800, app_height=600):
        self.widget = widget
        self.text = text
        self.tooltip = None
        self.app_width = app_width
        self.app_height = app_height
        self.widget.bind("<Enter>", self.show_tooltip)
        self.widget.bind("<Leave>", self.hide_tooltip)

        # Bind to the main window's movement
        self.widget.winfo_toplevel().bind("<Configure>", self.on_window_move)

    def show_tooltip(self, event=None):
        if self.tooltip:
            return
        self.tooltip = tk.Toplevel(self.widget)
        self.tooltip.wm_overrideredirect(True)

        label = tk.Label(self.tooltip, text=self.text, font=Font.main_font_12, background=Color.bg_color_yellow, relief="solid", borderwidth=0.1)
        label.pack()

        self.position_tooltip()

    def position_tooltip(self):
        if not self.tooltip:
            return

        self.tooltip.update_idletasks()  # Ensure tooltip size is updated
        tooltip_width = self.tooltip.winfo_width()
        tooltip_height = self.tooltip.winfo_height()

        # Get the position of the main window
        root_x = self.widget.winfo_toplevel().winfo_x()
        root_y = self.widget.winfo_toplevel().winfo_y()

        # Calculate center position relative to the main window
        x = root_x + (self.app_width // 2) - (tooltip_width // 2)
        y = root_y + (self.app_height // 2) - (tooltip_height // 2)

        self.tooltip.wm_geometry(f"+{x}+{y}")

    def hide_tooltip(self, event=None):
        if self.tooltip:
            self.tooltip.destroy()
            self.tooltip = None

    def on_window_move(self, event=None):
        if self.tooltip:
            self.position_tooltip()

