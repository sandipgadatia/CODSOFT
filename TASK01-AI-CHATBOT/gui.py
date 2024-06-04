

import tkinter as tk
from tkinter import scrolledtext
from chatbot import Chatbot

class ChatbotGUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Pizza Restaurant Chatbot")
        self.window.geometry("700x600")
        self.window.configure(bg='#1e1e1e')  # Darker background color

        self.chatbot = Chatbot()

        self.create_widgets()

    def create_widgets(self):
        # Create and pack widgets
        self.main_frame = tk.Frame(self.window, bg='#1e1e1e')
        self.main_frame.pack(expand=True, fill='both')

        self.chat_log = scrolledtext.ScrolledText(self.main_frame, state='disabled', wrap=tk.WORD, bg='#2e2e2e', fg='#e5ddd5', font=("Helvetica", 12), bd=0, padx=10, pady=10)
        self.chat_log.grid(row=0, column=0, padx=10, pady=10, sticky='nsew')

        self.entry_frame = tk.Frame(self.main_frame, bg='#1e1e1e')
        self.entry_frame.grid(row=1, column=0, padx=10, pady=10, sticky='ew')

        self.entry_box = tk.Entry(self.entry_frame, bg='#2e2e2e', fg='#e5ddd5', font=("Helvetica", 12), bd=0, insertbackground='#e5ddd5')
        self.entry_box.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 10), pady=5)
        self.entry_box.bind("<Return>", self.process_user_input)

        self.send_button = tk.Button(self.entry_frame, text="Send", command=self.process_user_input, bg='#075e54', fg='white', font=("Helvetica", 12), bd=0, activebackground='#128c7e', activeforeground='white', padx=10, pady=5)
        self.send_button.pack(side=tk.RIGHT)

        # Make the chat log and entry box resize with the window
        self.main_frame.rowconfigure(0, weight=1)
        self.main_frame.columnconfigure(0, weight=1)

    def process_user_input(self, event=None):
        user_input = self.entry_box.get()
        self.entry_box.delete(0, tk.END)

        self.update_chat_log(f"User: {user_input}")

        response = self.chatbot.get_response(user_input)
        self.update_chat_log(f"Bot: {response}")

    def update_chat_log(self, message):
        self.chat_log.config(state='normal')
        self.chat_log.insert(tk.END, message + "\n")
        self.chat_log.config(state='disabled')
        self.chat_log.yview(tk.END)

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    gui = ChatbotGUI()
    gui.run()

