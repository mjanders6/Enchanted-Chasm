
from tkinter import *
import tkinter as tk
from tkinter import ttk
from Class.board import Game_Board
from Class.cell import Cell
from Utilities import settings


class gui_txtbox(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)
        self.create_text_object = None

    @staticmethod
    def create_text_object(location):
        return Text(location, height=8, width=42)

    @staticmethod
    def log_capture(text):
        text.insert(tk.INSERT, f'This is the game log:' + '\n')
        for index, value in Game_Board.GAME_TEXT.items():
            text.insert(tk.INSERT, f'{value}' + '\n')

