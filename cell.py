from tkinter import Button, Label
import random
import settings
import utils
class Cell:
    all = []
    master_obs = {}
    cell_count = settings.CELL_COUNT
    cell_count_label_object = None
    MASTER_BOARD = []
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
            width=12,
            height=4,
            state="disabled",
            text= ''
        )
        btn.bind('<Button-1>', self.left_click_actions ) # left click
        btn.bind('<Button-3>', self.right_click_actions) # right click
        self.cell_btn_object = btn

    def left_click_actions(self, event):
        print(f'({self.x}, {self.y})')
        h_cur = Cell.master_obs['H']
        # works, just need to be able
        # to upate board and update previous H
        if self.status == 'E':
            Cell.MASTER_BOARD[h_cur[0]][h_cur[1]] = '*'
            Cell.master_obs['H'] = (self.x, self.y)
            Cell.MASTER_BOARD[self.x][self.y] = 'H'
            self.status = 'H'
            # Cell.set_players()

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
        print(self.status)

    @staticmethod
    def randomize_mines():
        picked_cells = random.sample(
            Cell.all, settings.MINES_COUNT
        )
        for picked_cells in picked_cells:
            picked_cells.is_mine = True
            print(picked_cells)

    # Sets the status of the cell to the obstacle value
    # def set_players(MASTER_OBSTACLES):
    #     Cell.master_obs = {key: tuple(value) for key, value in MASTER_OBSTACLES.items()}
    #     for cells in Cell.all:
    #         for key, value in Cell.master_obs.items():
    #             if value == (cells.x, cells.y):
    #                 print(cells)
    #                 cells.is_mine = True
    #                 cells.status = key
    #                 if key == 'H':
    #                     cells.cell_btn_object.configure(text=key)
    #                     for i in cells.surrounded_cells:
    #                         i.cell_btn_object.configure(state='normal')

    @staticmethod
    def set_players():
        for cells in Cell.all:
            row = len(Cell.MASTER_BOARD)
            i = 0
            while i < row:
                j = 0
                col = len(Cell.MASTER_BOARD[i])
                while j < col:
                    if (cells.x, cells.y) == (i, j):
                        cells.status = Cell.MASTER_BOARD[i][j]
                        # cells.cell_btn_object.configure(state='disabled')
                        # cells.is_last_move = False
                        # cells.is_mine = False
                        if Cell.MASTER_BOARD[i][j] == 'T' or Cell.MASTER_BOARD[i][j] == 'M' or Cell.MASTER_BOARD[i][j] == 'P':
                            cells.is_mine = True
                        if Cell.MASTER_BOARD[i][j] == '*':
                            cells.is_last_move = True
                            cells.is_mine = False
                            cells.cell_btn_object.configure(state='disabled')
                            cells.cell_btn_object.configure(text=Cell.MASTER_BOARD[i][j])
                        if Cell.MASTER_BOARD[i][j] == 'H':
                            cells.is_mine = False
                            cells.cell_btn_object.configure(text=Cell.MASTER_BOARD[i][j])
                            for k in cells.surrounded_cells:
                                k.cell_btn_object.configure(state='normal')

                    j += 1
                i += 1

    # @staticmethod
    # def set_board():
    #     rows = len(Cell.MASTER_BOARD)
    #     i = 0
    #     while i < rows:
    #         cols = len(Cell.MASTER_BOARD[i])
    #         j = 0
    #         while j < cols:
    #             Cell.MASTER_BOARD[i][j]
    #             j += 1
    #         i += 1

    def get_cell_by_axis(self, x,y):
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