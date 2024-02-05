from tkinter import Button, Label
import settings
import utils


class Cell:
    all = []
    cell_count = settings.CELL_COUNT
    cell_count_label_object = None

    def __init__(self, x, y, is_mine=False):
        self.is_mine = is_mine
        self.is_opened = False
        self.cell_btn_object = None
        self.x = x
        self.y = y
        # Append the object to the Cell.all list
        Cell.all.append(self)

    def create_btn_object(self, location):
        btn = Button(
            location,
            width=12,
            height=4,
        )
        btn.bind('<Button-1>', self.left_click_actions ) # left click
        btn.bind('<Button-3>', self.right_click_actions) # right click
        self.cell_btn_object = btn

    def get_cell_by_axis(self, x, y):
        # Return a cell object based on the value of x,y
        for cell in Cell.all:
            if cell.x == x and cell.y == y:
                return cell

    def left_click_actions(self, event):
        print(self.__repr__())

    def right_click_actions(self, event):
        print('right click')

    def __repr__(self):
        return f"Cell({self.x}, {self.y})"