import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from src.utils.component import Component
from src.utils.constant import ImageUrl, Auth, Api, Font, ToolTip, Color
from src.utils.file import FileManager
import requests  # Thêm thư viện requests để gọi API

class ShareListScreen(tk.Frame):
    def __init__(self, master, callback_list, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        self.bg_photo = None
        self.bg_image = None
        self.canvas = None
        self.main_frame = None
        self.tree = None
        self.master = master
        self.show_share_screen = callback_list["ShareScreen"]

        # Load the background image
        self.bg_image = Image.open(FileManager().resource_path(ImageUrl.bg_share_list_screen))
        self.bg_photo = ImageTk.PhotoImage(self.bg_image)
        # self.load_widgets()
        # self.fetch_and_populate_data()  # Gọi phương thức này sau khi load widgets

    def load_widgets(self):

        # Create a canvas and put the image on it
        self.canvas = tk.Canvas(self, width=self.bg_image.width, height=self.bg_image.height)
        self.canvas.pack(fill=tk.BOTH, expand=True)
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.bg_photo)

        # Main content frame
        self.main_frame = tk.Frame(self.canvas, bg=Color.bg_color_blue, bd=2, relief=tk.RAISED)
        self.main_frame.place(relx=0.1, rely=0.11, relwidth=0.8, relheight=0.8)

        # Left frame for Treeview
        left_frame = tk.Frame(self.main_frame, bg=Color.bg_color_blue)
        left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Treeview
        self.tree = ttk.Treeview(left_frame, columns=("ID", "Title"), show='headings', height=20, selectmode='browse')
        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Scrollbar for Treeview
        scrollbar = ttk.Scrollbar(left_frame, orient=tk.VERTICAL, command=self.tree.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.tree.configure(yscrollcommand=scrollbar.set)

        # Configure Treeview columns
        self.tree.heading("ID", text="ID")
        self.tree.heading("Title", text="Tiêu đề")
        self.tree.column("ID", width=50, anchor=tk.CENTER)
        self.tree.column("Title", width=200, anchor=tk.W)

        # Bind select events
        self.tree.bind('<<TreeviewSelect>>', self.on_item_select)

        # Right frame for details
        self.right_frame = tk.Frame(self.main_frame, bg=Color.bg_color_yellow)
        self.right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Detail title
        self.detail_title = tk.Label(self.right_frame, text="Chi tiết", font=Font.main_font, bg=Color.bg_color_yellow)
        self.detail_title.pack(pady=10)

        # Detail content
        self.detail_content = tk.Text(self.right_frame, wrap=tk.WORD, font=Font.main_font, height=15, bg='#ffffff', state='disabled')
        self.detail_content.pack(fill=tk.BOTH, expand=True)

        # Ensure the right frame is visible
        self.right_frame.update()
        self.right_frame.lift()
        self.fetch_and_populate_data()  # Gọi phương thức này sau khi load widgets

        Component.left_label(self)
        Component.right_button_back(self, self.show_share_screen)
        Component.right_button_intro(self, ToolTip.share_screen)

    def on_item_select(self, event):
        selected_item = self.tree.focus()
        if selected_item:
            self.update_detail_view(selected_item)
        else:
            print("No item selected")

    def update_detail_view(self, selected_item):
        item_data = self.tree.item(selected_item)
        print(f"Item data: {item_data}")  # Debug print
        if 'values' in item_data:
            item_id, item_title = item_data['values']
            print(f"Updating details for: ID={item_id}, Title={item_title}")  # Debug print

            self.detail_title.config(text=f"Details: {item_title}")
            print(f"Detail title updated to: {self.detail_title['text']}")  # Debug print

            self.detail_content.delete('1.0', tk.END)
            self.detail_content.insert(tk.END, f"ID: {item_id}\n\n")
            self.detail_content.insert(tk.END, f"Title: {item_title}\n\n")
            self.detail_content.insert(tk.END, "Content:\n")
            self.detail_content.insert(tk.END, f"This is the detailed content for {item_title}. "
                                               "You can add any additional information here.")
            print(f"Detail content updated. Current content: {self.detail_content.get('1.0', tk.END)}")  # Debug print

            self.detail_title.update()
            self.detail_content.update()

            print("Detail view updated")  # Debug print
        else:
            print("No values found for selected item")  # Debug print

    def fetch_data_from_api(self):
        try:
            response = requests.get(Api.get_share_list)  # Thay thế bằng URL API thực tế của bạn
            if response.status_code == 200:
                return response.json()
            else:
                print(f"Failed to fetch data: {response.status_code}")
                return None
        except Exception as e:
            print(f"Error fetching data: {e}")
            return None

    def fetch_and_populate_data(self):
        data = self.fetch_data_from_api()
        if data:
            self.populate_tree(data)
        else:
            print("Using sample data due to API fetch failure")

    def populate_tree(self, data):
        # Clear existing items
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Add data from API
        for item in data:
            self.tree.insert("", "end", values=(item['id'], item['title']))

        print(f"Populated tree with {len(self.tree.get_children())} items from API")

