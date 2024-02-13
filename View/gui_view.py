from tkinter import *
import tkinter as tk
from tkinter import ttk
from Utilities import settings, utils

class View(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        # create widgets
        # Top frame
        self.top_frame = Frame(self, bg='gray', width=settings.WIDTH, height=utils.height_prct(25))
        self.top_frame.place(x=0, y=0)
        self.head_label = ttk.Label(top_frame, text='The Enchanted Chasm', font=('typewriter', 40), background='grey')
        self.head_label.place(x=utils.width_prct(25), y=utils.height_prct(10))