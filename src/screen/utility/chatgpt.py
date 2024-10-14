import tkinter as tk
from tkinter import scrolledtext
import requests
import threading
import queue

class ChatGPTApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("GPT-4o Mini Chat App")
        self.geometry("600x400")

        self.chat_history = scrolledtext.ScrolledText(self, state='disabled')
        self.chat_history.pack(expand=True, fill='both')

        self.user_input = tk.Entry(self)
        self.user_input.pack(expand=True, fill='x')

        self.send_button = tk.Button(self, text="Gửi", command=self.send_message)
        self.send_button.pack()

        self.user_input.bind("<Return>", lambda event: self.send_message())

        self.queue = queue.Queue()
        self.after(100, self.check_queue)

    def send_message(self):
        user_message = self.user_input.get()
        if not user_message:
            return
        self.user_input.delete(0, tk.END)
        self.update_chat_history(f"Bạn: {user_message}")

        threading.Thread(target=self.get_response, args=(user_message,), daemon=True).start()

    def update_chat_history(self, message):
        self.chat_history.config(state='normal')
        self.chat_history.insert(tk.END, message + "\n\n")
        self.chat_history.config(state='disabled')
        self.chat_history.see(tk.END)

    def get_response(self, message):
        try:
            response = self.get_gpt4o_mini_response(message)
            self.queue.put(("GPT-4o Mini: " + response))
        except Exception as e:
            self.queue.put(("Lỗi: " + str(e)))

    def check_queue(self):
        try:
            while True:
                message = self.queue.get_nowait()
                self.update_chat_history(message)
        except queue.Empty:
            pass
        finally:
            self.after(100, self.check_queue)

    def get_gpt4o_mini_response(self, message):
        url = "https://huynhthao-duckduckgo-95.deno.dev/v1/chat/completions"
        headers = {
            "Authorization": "Bearer YOUR_API_KEY_HERE",
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
        return response.json()['choices'][0]['message']['content']

if __name__ == "__main__":
    app = ChatGPTApp()
    app.mainloop()