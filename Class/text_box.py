
from tkinter import *
import tkinter as tk
from tkinter import ttk
from Class.board import Game_Board



class gui_txtbox(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)
        self.create_text_object = None

    @staticmethod
    def create_text_object(location):
        tb = Text(location, height=8, width=42)
        tb.place(x=5, y=60)
        tb.insert(tk.INSERT, f'This is the game log:' + '\n')
        Game_Board.get_game_text(tb)

    @staticmethod
    def log_capture(text):
        text.insert(tk.INSERT, f'This is the game log:' + '\n')
        value = Game_Board.get_game_text()
        text.insert(tk.INSERT, f'{value}' + '\n')

