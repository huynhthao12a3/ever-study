﻿import tkinter as tk
from tkinter import scrolledtext
import requests
import threading
import queue
from src.utils.component import Component
from src.utils.constant import ImageUrl, ToolTip
from src.utils.gif import AnimatedGifCanvas
from googletrans import Translator

class ChatAIScreen(tk.Frame):
    def __init__(self, master, callback_list, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.master = master
        self.show_utility_screen = callback_list["UtilityScreen"]
        self.queue = queue.Queue()
        self.input_var = tk.StringVar()
        self.loading_animation = None
        self.after(100, self.check_queue)
        self.everstudy_api_url = "https://everstudy-chat-api.vercel.app/search"

    def load_widgets(self):
        # Background
        bg_path = ImageUrl.bg_time_table_screen
        self.bg_canvas = AnimatedGifCanvas(self, bg_path, self.on_click)
        self.bg_canvas.pack(fill='both', expand=True)

        # Chat history frame
        chat_frame = tk.Frame(self, bg='#f0f0f0', bd=0.1, relief='groove')
        chat_frame.place(relx=0.07, rely=0.11, relwidth=0.86, relheight=0.68)

        self.chat_history = scrolledtext.ScrolledText(chat_frame, state='normal', bg='#ffffff', font=('Arial', 10))
        self.chat_history.pack(padx=10, pady=10, fill='both', expand=True)
        self.chat_history.insert(tk.END, "\n                                                  ***** Chào mừng bạn đến với EverStudy AI *****\n\n")
        self.chat_history.config(state='disabled')

        # Input frame
        input_frame = tk.Frame(self, bg='#e0e0e0', bd=0.1, relief='groove')
        input_frame.place(relx=0.07, rely=0.82, relwidth=0.86, relheight=0.08)

        self.user_input = tk.Entry(input_frame, font=('Arial', 12), bd=1, relief='solid', textvariable=self.input_var)
        self.user_input.pack(side='left', padx=(10, 5), pady=10, fill='both', expand=True)

        self.send_button = tk.Button(input_frame, text="Gửi", command=self.send_message,
                                     bg='#4CAF50', fg='white', font=('Arial', 10, 'bold'))
        self.send_button.pack(side='right', padx=(5, 10), pady=10, ipadx=10)

        self.user_input.bind("<Return>", lambda event: self.send_message())

        # Back button
        Component.right_button_back(self, self.show_utility_screen)
        Component.right_button_intro(self, ToolTip.chat_gpt_screen)

    def on_click(self, x, y):
        print(f"Clicked at: {x}, {y}")

    def send_message(self):
        user_message = self.input_var.get().strip()

        if not user_message:
            print("No message to send")
            return

        self.input_var.set('')  # Clear the input
        self.update_chat_history(f"Bạn: {user_message}")
        self.start_loading_animation()
        threading.Thread(target=self.get_response, args=(user_message,), daemon=True).start()

    def update_chat_history(self, message):
        self.chat_history.config(state='normal')
        self.chat_history.insert(tk.END, "\n=> " + message + "\n\n")
        self.chat_history.config(state='disabled')
        self.chat_history.see(tk.END)

    def start_loading_animation(self):
        self.loading_animation = "."
        self.update_loading_animation()

    def update_loading_animation(self):
        if self.loading_animation:
            self.chat_history.config(state='normal')
            self.chat_history.insert(tk.END, f"{self.loading_animation}" + "." * (len(self.loading_animation) % 4))
            self.chat_history.delete(tk.END + "-2c", tk.END)
            self.chat_history.config(state='disabled')
            self.chat_history.see(tk.END)
            self.after(200, self.update_loading_animation)

    def stop_loading_animation(self):
        if self.loading_animation:
            self.chat_history.config(state='normal')
            self.chat_history.delete("end-2l", "end-1c")
            self.chat_history.config(state='disabled')
            self.loading_animation = None

    def get_response(self, message):
        try:
            response = self.search_duckduckgo(message)
            if response:
                formatted_response = self.format_search_results(response)
                self.queue.put(("EverStudy AI: " + formatted_response))
            else:
                self.queue.put("EverStudy AI: Xin lỗi, tôi không tìm thấy thông tin phù hợp.")
        except Exception as e:
            print(f"Error getting response: {str(e)}")
            self.queue.put("Lỗi: EverStudy AI đang gặp sự cố. Vui lòng thử lại sau.")

    def check_queue(self):
        try:
            while True:
                message = self.queue.get_nowait()
                self.stop_loading_animation()
                self.update_chat_history(message)
        except queue.Empty:
            pass
        finally:
            self.after(100, self.check_queue)

    def get_gpt4o_mini_response(self, message):
        url = "https://everstudy-chat-ai.vercel.app/v1/chat/completions"
        headers = {
            # "Authorization": "Bearer EverStudy",
            "Content-Type": "application/json"
        }
        data = {
            "model": "gpt-4o-mini",
            "messages": [
                {"role": "system", "content": "Bạn là một trợ lý AI hữu ích."},
                {"role": "user", "content": message}
            ]
        }
        response = requests.post(url, json=data, headers=headers)
        response.raise_for_status()
        print(response.json())
        return response.json()['choices'][0]['message']['content']

    def search_duckduckgo(self, query, max_results=1):
        """
        Tìm kiếm trên DuckDuckGo bằng API của Everstudy.
        """
        url = f"{self.everstudy_api_url}?q={query}&lang=vi&max_results={max_results}"
        print(url)
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            data = response.json()
            return data["results"]
        except requests.exceptions.RequestException as e:
            print(f"Lỗi khi gọi API DuckDuckGo: {e}")
            return None

    def format_search_results(self, results):
        """
        Định dạng kết quả tìm kiếm thành một chuỗi dễ đọc.
        """
        formatted = "" #"Đây là một số thông tin tôi tìm thấy:\n\n"
        translator = Translator()
        for result in results:
            # formatted += f"Tiêu đề: {result['title']}\n"
            formatted += f"{translator.translate(result['body'], dest='vi').text}\n"
            # formatted += f"URL: {result['href']}\n\n"
        return formatted
    