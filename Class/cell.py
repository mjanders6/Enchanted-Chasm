'''
Buttons/Cells
- holds x,y location
- holds status
- binds clicking
'''

from tkinter import Button
import random
from Class.board import Game_Board
from Utilities import settings

class Cell:
    all = []
    all2 = []
    cell_count = settings.CELL_COUNT
    cell_count_label_object = None

    def __init__(self, x, y, is_mine=False, is_last_move=False):
        self.is_mine = is_mine
        self.is_last_move = is_last_move
        self.is_opened = False
        self.cell_btn_object = None
        self.status = ''
        self.x = x
        self.y = y
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
        btn.bind('<Button-1>', self.left_click_actions ) # left click
        btn.bind('<Button-3>', self.right_click_actions) # right click
        self.cell_btn_object = btn

    def left_click_actions(self, event):
        print(f'({self.x}, {self.y})')
        h_cur = Game_Board.MASTER_OBSTACLES['H']
        # works, just need to be able
        # to upate board and update previous H
        if self.status == 'E' and self.cell_btn_object['state'] == 'normal':
            Game_Board.MASTER_BOARD[h_cur[0]][h_cur[1]] = '*'
            Game_Board.MASTER_OBSTACLES['H'] = (self.x, self.y)
            Game_Board.MASTER_BOARD[self.x][self.y] = 'H'
            self.status = 'H'
            Cell.set_players()

        if self.is_mine and self.cell_btn_object['state'] == 'normal' and self.status != 'H':
            self.show_mine()

        if self.is_mine and self.cell_btn_object['state'] == 'normal' and self.status == 'T':
            self.show_treasure()

        if self.cell_btn_object['state'] == 'normal' and self.status != 'H' and self.status == 'W':
            self.show_wall()

        Cell.set_players()

    def show_mine(self):
        self.cell_btn_object.configure(bg='red')
        self.cell_btn_object.configure(text=self.status)

    def show_treasure(self):
        self.cell_btn_object.configure(bg='green')
        self.cell_btn_object.configure(text=self.status)

    def show_wall(self):
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

    def right_click_actions(self, event):
        print(f'({self.x}, {self.y})')
        print(self.cell_btn_object['state'])

    @staticmethod
    def randomize_mines():
        picked_cells = random.sample(
            Cell.all, settings.MINES_COUNT
        )
        for picked_cells in picked_cells:
            picked_cells.is_mine = True
            print(picked_cells)

    @staticmethod
    def set_players():
        for cells in Cell.all:
            row = len(Game_Board.MASTER_BOARD)
            i = 0
            while i < row:
                j = 0
                col = len(Game_Board.MASTER_BOARD[i])
                while j < col:
                    if (cells.x, cells.y) == (i, j):
                        cells.status = Game_Board.MASTER_BOARD[i][j]
                        # cells.cell_btn_object.configure(state='disabled')
                        if Game_Board.MASTER_BOARD[i][j] == 'H':
                            cells.is_mine = False
                            cells.cell_btn_object.configure(text=Game_Board.MASTER_BOARD[i][j])
                            for k in cells.surrounded_cells:
                                k.cell_btn_object.configure(state='normal')
                        if Game_Board.MASTER_BOARD[i][j] == '*':
                            cells.is_last_move = True
                            cells.is_mine = False
                            cells.cell_btn_object.configure(state='normal')
                            cells.cell_btn_object.configure(text=Game_Board.MASTER_BOARD[i][j])
                        if Game_Board.MASTER_BOARD[i][j] == 'T' or Game_Board.MASTER_BOARD[i][j] == 'M' or Game_Board.MASTER_BOARD[i][j] == 'P' or Game_Board.MASTER_BOARD[i][j] == 'W':
                            cells.is_mine = True
                            cells.cell_btn_object.configure(state='normal')

                    j += 1
                i += 1

    # @staticmethod
    # def set_players():
    #     for cells in Cell.all:
    #         row = len(Game_Board.MASTER_BOARD)
    #         i = 0
    #         while i < row:
    #             j = 0
    #             col = len(Game_Board.MASTER_BOARD[i])
    #             while j < col:
    #                 if (cells.x, cells.y) == (i, j):
    #                     cells.status = Game_Board.MASTER_BOARD[i][j]
    #                     cells.cell_btn_object.configure(state='disabled')
    #                     if Game_Board.MASTER_BOARD[i][j] == 'T' or Game_Board.MASTER_BOARD[i][j] == 'M' or Game_Board.MASTER_BOARD[i][j] == 'P' or Game_Board.MASTER_BOARD[i][j] == 'W':
    #                         cells.is_mine = True
    #                         cells.cell_btn_object.configure(state='normal')
    #                     if Game_Board.MASTER_BOARD[i][j] == '*':
    #                         cells.is_last_move = True
    #                         cells.is_mine = False
    #                         cells.cell_btn_object.configure(state='normal')
    #                         cells.cell_btn_object.configure(text=Game_Board.MASTER_BOARD[i][j])
    #                     if Game_Board.MASTER_BOARD[i][j] == 'H':
    #                         cells.is_mine = False
    #                         cells.cell_btn_object.configure(text=Game_Board.MASTER_BOARD[i][j])
    #                         for k in cells.surrounded_cells:
    #                             k.cell_btn_object.configure(state='normal')
    #
    #                 j += 1
    #             i += 1

    def get_cell_by_axis(self, x, y):
        # Return a cell object based on the value of x,y
        for cell in Cell.all:
            if cell.x == x and cell.y == y:
                return cell

    @property
    def surrounded_cells(self):
        cells = [
            self.get_cell_by_axis(self.x - 1, self.y),
            self.get_cell_by_axis(self.x, self.y - 1),
            self.get_cell_by_axis(self.x + 1, self.y),
            self.get_cell_by_axis(self.x, self.y + 1)
        ]

        cells = [cell for cell in cells if cell is not None]
        return cells

    def __repr__(self):
        return f"Cell({self.x}, {self.y})"