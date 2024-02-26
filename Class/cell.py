'''
Buttons/Cells
- holds x,y location
- holds status
- binds clicking
'''

from tkinter import Button, messagebox
from tkinter import *
import sys
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

            Cell.set_players()

        if Game_Board.btns[row][col]['state'] == 'normal' and Game_Board.MASTER_BOARD[row][col] == 'M':
            Cell.show_monster(row, col)

        if Game_Board.btns[row][col]['state'] == 'normal' and Game_Board.MASTER_BOARD[row][col] == 'P':
            Cell.show_pit(row, col)

        if Game_Board.btns[row][col]['state'] == 'normal' and Game_Board.MASTER_BOARD[row][col] == 'T':
            Cell.show_treasure(row, col)

        if Game_Board.btns[row][col]['state'] == 'normal' and Game_Board.MASTER_BOARD[row][col] == 'W':
            Cell.show_wall(row, col)

    @staticmethod
    def show_monster(row, col):
        Game_Board.btns[row][col].configure(bg='red')
        Game_Board.btns[row][col].configure(text='M')
        Cell.game_over_monster()

    @staticmethod
    def show_pit(row, col):
        Game_Board.btns[row][col].configure(bg='red')
        Game_Board.btns[row][col].configure(text='P')
        Cell.game_over_pit()

    @staticmethod
    def show_treasure(row, col):
        Game_Board.btns[row][col].configure(bg='green')
        Game_Board.btns[row][col].configure(text='T')
        Cell.you_win()

    @staticmethod
    def show_wall(row, col):
        Game_Board.btns[row][col].configure(bg='brown')
        Game_Board.btns[row][col].configure(state='disabled')
        Game_Board.btns[row][col].configure(text='W')

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
    def game_over_monster():
        messagebox.showinfo(title='The Monster Killed You!', message='You have found the monster! You are now dead!\n :-( so sad')
        sys.exit()

    @staticmethod
    def game_over_pit():
        messagebox.showinfo(title='You fell in the Pit!', message='You have found the Pit! You are now dead!\n :-( so sad')
        sys.exit()

    @staticmethod
    def you_win():
        messagebox.showinfo(title='You Win!', message='You have found the treasure! Level mastered!\n :-) your amazing')
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

        # for (row, col) in cells:

        return cells

    @staticmethod
    def m_obs():
        h = Game_Board.MASTER_OBSTACLES['H']
        cells = [
            Game_Board.MASTER_BTN_BOARD[(h[0] - 2, h[1])],
            Game_Board.MASTER_BTN_BOARD[(h[0], h[1] - 2)],
            Game_Board.MASTER_BTN_BOARD[(h[0] + 2, h[1])],
            Game_Board.MASTER_BTN_BOARD[(h[0], h[1] + 2)]
        ]
        cells = [cell for cell in cells if cell is not None]

        if 'M' in cells:
            return 'You are close to a monster'

    @staticmethod
    def m_obs_to_close():
        h = Game_Board.MASTER_OBSTACLES['H']
        cells = [
            Game_Board.MASTER_BTN_BOARD[(h[0] - 1, h[1])],
            Game_Board.MASTER_BTN_BOARD[(h[0], h[1] - 1)],
            Game_Board.MASTER_BTN_BOARD[(h[0] + 1, h[1])],
            Game_Board.MASTER_BTN_BOARD[(h[0], h[1] + 1)]
        ]
        cells = [cell for cell in cells if cell is not None]

        if 'M' in cells:
            return 'You are way to close to a monster! Proceed with caution!'

    @staticmethod
    def p_obs():
        h = Game_Board.MASTER_OBSTACLES['H']
        cells = [
            Game_Board.MASTER_BTN_BOARD[(h[0] - 1, h[1])],
            Game_Board.MASTER_BTN_BOARD[(h[0], h[1] - 1)],
            Game_Board.MASTER_BTN_BOARD[(h[0] + 1, h[1])],
            Game_Board.MASTER_BTN_BOARD[(h[0], h[1] + 1)]
        ]
        cells = [cell for cell in cells if cell is not None]

        if 'P' in cells:
            return 'You are close to the Pit'

    @classmethod
    def log_obs(cls):
        if cls.p_obs() != None:
            return cls.p_obs()

        if cls.m_obs_to_close() != None:
            return cls.m_obs_to_close()

        if cls.m_obs() != None:
            return cls.m_obs()

    def __repr__(self):
        return f"Cell({self.x}, {self.y})"