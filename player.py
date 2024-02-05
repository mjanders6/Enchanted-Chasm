from tkinter import Button, Label
import random
import settings
import utils
import cell as Cell
class Player:

    def __init__(self):
        self.status = ''
        self.cell = ()



    def set_players(MASTER_OBSTACLES):
        Cell.master_obs = {key: tuple(value) for key, value in MASTER_OBSTACLES.items()}
        for cells in Cell.all:
            for key, value in Cell.master_obs.items():
                if value == (cells.x, cells.y):
                    cells.is_mine = True
                    cells.status = key
                    if key == 'H':
                        cells.cell_btn_object.configure(text=key)
                        for i in cells.surrounded_cells:
                            i.cell_btn_object.configure(state='normal')

