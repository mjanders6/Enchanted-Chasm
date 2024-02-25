'''
Buttons/Cells
- holds x,y location
- holds status
- binds clicking
'''

from tkinter import Button, messagebox
from tkinter import *
import sys
import random
from functools import partial
from Class.board import Game_Board

from Utilities import settings

class Cell():
    all = []
    all2 = []
    cell_count = settings.CELL_COUNT
    cell_count_label_object = None
    click = 0

    def __init__(self, x, y, is_mine=False, is_last_move=False):
        self.is_mine = is_mine
        self.is_last_move = is_last_move
        self.is_opened = False
        self.cell_btn_object = None
        self.status = ''
        self.x = x
        self.y = y
        self.text_contents = ""
        # Append the object to the Cell.all list
        Cell.all.append(self)

    def create_btn_object(self, location):
        btn = Button(
            location,
            width=3,
            height=1,
            state="disabled",
            text= ''
        )
        # btn.bind('<Button-1>', self.left_click_actions ) # left click
        btn["command"] = partial(self.clicked, btn)
        self.cell_btn_object = btn

    def clicked(self, button: Button):
        h_cur = Game_Board.MASTER_OBSTACLES['H']
        # works, just need to be able
        # to upate board and update previous H
        if self.status == 'E' and self.cell_btn_object['state'] == 'normal':
            Game_Board.MASTER_BOARD[h_cur[0]][h_cur[1]] = '*'
            Game_Board.MASTER_OBSTACLES['H'] = (self.x, self.y)
            Game_Board.MASTER_BOARD[self.x][self.y] = 'H'
            self.status = 'H'
            Cell.set_players()

        if self.is_mine and self.cell_btn_object['state'] == 'normal' and self.status == 'M':
            self.show_monster()

        if self.is_mine and self.cell_btn_object['state'] == 'normal' and self.status == 'P':
            self.show_pit()

        if self.is_mine and self.cell_btn_object['state'] == 'normal' and self.status == 'T':
            self.show_treasure()

        if self.cell_btn_object['state'] == 'normal' and self.status != 'H' and self.status == 'W':
            self.show_wall()

        Cell.set_players()

    @staticmethod
    def cell_click(row, col):
        h_cur = Game_Board.MASTER_OBSTACLES['H']
        # works, just need to be able
        # to upate board and update previous H
        if Game_Board.MASTER_BTN_BOARD[(row, col)] == 'E' and Game_Board.btns[row][col]['state'] == 'normal':
            Game_Board.MASTER_BOARD[h_cur[0]][h_cur[1]] = '*'
            Game_Board.MASTER_OBSTACLES['H'] = (row, col)
            Game_Board.MASTER_BOARD[row][col] = 'H'
            # self.status = 'H'
            Cell.set_players()

        if Game_Board.btns[row][col]['state'] == 'normal' and Game_Board.MASTER_BOARD[row][col] == 'M':
            Game_Board.btns[row][col]['text'] = 'M'
            Cell.set_players()

    def left_click_actions(self, event):
        print(self.__dict__)
        h_cur = Game_Board.MASTER_OBSTACLES['H']
        # works, just need to be able
        # to upate board and update previous H
        if self.status == 'E' and self.cell_btn_object['state'] == 'normal':
            Game_Board.MASTER_BOARD[h_cur[0]][h_cur[1]] = '*'
            Game_Board.MASTER_OBSTACLES['H'] = (self.x, self.y)
            Game_Board.MASTER_BOARD[self.x][self.y] = 'H'
            self.status = 'H'
            Cell.set_players()

        if self.is_mine and self.cell_btn_object['state'] == 'normal' and self.status == 'M':
            self.show_monster()

        if self.is_mine and self.cell_btn_object['state'] == 'normal' and self.status == 'T':
            self.show_treasure()

        if self.cell_btn_object['state'] == 'normal' and self.status != 'H' and self.status == 'W':
            self.show_wall()

        Cell.set_players()


    def show_monster(self):
        self.cell_btn_object.configure(bg='red')
        self.cell_btn_object.configure(text=self.status)
        Cell.game_over()

    def show_pit(self):
        self.cell_btn_object.configure(bg='red')
        self.cell_btn_object.configure(text=self.status)
        Cell.game_over()

    def show_treasure(self):
        self.cell_btn_object.configure(bg='green')
        self.cell_btn_object.configure(text=self.status)
        Cell.you_win()

    def show_wall(self):
        Game_Board.action_call('You hit a wall')
        self.cell_btn_object.configure(bg='brown')
        self.cell_btn_object.configure(state='disabled')
        self.cell_btn_object.configure(text=self.status)

    def show_cell(self):
        if not self.is_opened:
                        # If this was a mine candidate, then for safety, we should
            # configure the background color to SystemButtonFace
            self.cell_btn_object.configure(
                bg='SystemButtonFace'
            )
            # Mark the cell as opened (Use is as the last line of this method)
        self.is_opened = True

    @staticmethod
    def set_players(): # refactor to make everything rely on the Game_Boar. Replace
        for i in range(len(Game_Board.btns)):
            for j in range(len(Game_Board.btns[i])):
                row = Game_Board.btns[i][j].grid_info()['row']
                col = Game_Board.btns[i][j].grid_info()['column']
                if (row, col) == (i, j):
                    # cells.status = Game_Board.MASTER_BOARD[i][j]
                    # cells.cell_btn_object.configure(state='disabled')
                    if Game_Board.MASTER_BOARD[i][j] == 'H':
                        Game_Board.btns[i][j].configure(text=Game_Board.MASTER_BOARD[i][j])
                        for (row, col) in Cell.surrounded_cells():
                            Game_Board.btns[row][col].configure(state='normal')
                    if Game_Board.MASTER_BOARD[i][j] == '*':
                        Game_Board.btns[row][col].configure(state='normal')
                        Game_Board.btns[row][col].configure(text=Game_Board.MASTER_BOARD[i][j])

    @staticmethod
    def print_tex():
        l = ['list 1', 'list 2']
        return l

    @staticmethod
    def game_over():
        messagebox.showinfo(title='Monster Killed You!', message='You have found the monster! You are now dead!\n :-( so sad')
        sys.exit()

    @staticmethod
    def you_win():
        messagebox.showinfo(title='You Win!', message='You have found the treasure!\nYou have mastered this level!\n :-) your amazing')
        sys.exit()


    def get_cell_by_axis(self):
        # Return a cell object based on the value of x,y
        for cell in Cell.all:
            if cell.x == x and cell.y == y:
                return cell

    @staticmethod
    def surrounded_cells():
        h = Game_Board.MASTER_OBSTACLES['H']
        cells = [
            (h[0] - 1, h[1]),
            (h[0], h[1] - 1),
            (h[0] + 1, h[1]),
            (h[0], h[1] + 1)
        ]

        cells = [cell for cell in cells if cell is not None]
        return cells


    def __repr__(self):
        return f"Cell({self.x}, {self.y})"