import tkinter as tk
from tkinter import ttk, Button
from itertools import product
from functools import partial
from Class.cell import Cell
from Class.board import Game_Board
from Utilities import settings

MASTER_BOARD = []
all = []
MASTER_OBSTACLES = {}

class Model:
    def __init__(self):
        self.text_contents = ""

    def set_text_contents(self, new_contents):
        self.text_contents = new_contents

    Game_Board.init_board('TheCave.txt')
    Game_Board.obstacle_locations()
    Game_Board.spawn_object('H')
    Game_Board.button_locations()

class View:
    def __init__(self, root, controller):
        self.root = root
        self.controller = controller

        # create window for grids
        root.columnconfigure(0, weight=4)
        root.columnconfigure(1, weight=4)
        root.geometry('1300x600+50+50')

        self.head_label = ttk.Label(root, text='The Enchanted Chasm', font=('typewriter', 40))
        self.head_label.grid(column=0, row=0, columnspan=2)

        # add frames to the window
        self.left_frame = ttk.Frame(root, height=25, width=500)
        self.left_frame.grid(column=0, row=1, sticky=tk.EW)

        # Place the button in a grid
        controller.button_obj(self.left_frame)

        # add widgets to each frame

        # Create a Text widget
        self.text_widget = tk.Text(root)
        self.text_widget.grid(column=1, row=1, sticky=tk.NE)

    def update_text_contents(self, new_contents):
        # Update the Text widget with the new text contents
        # self.text_widget.delete("1.0", tk.END)
        self.text_widget.insert("1.0", new_contents + "\n")



class Controller:
    def __init__(self, root):
        self.root = root
        self.model = Model()
        self.view = View(root, self)
        self.cell_btn_object = []

    def set_text_contents(self):
        new_contents = 'new text'  # Define the new contents of the Text widget
        self.model.set_text_contents(new_contents)  # Update the model with the new contents
        self.view.update_text_contents(new_contents)  # Update the view with the new contents



    # def button_obj(self, location):
    #     global all
    #     for number, (col, row) in enumerate(product(range(20), range(20))):
    #         button = Button(location,
    #                         width=3,
    #                         height=1,
    #                         state="normal",
    #                         text=''
    #                         )
    #         # callback, which also submits the button innstance to the function
    #         button["command"] = partial(self.clicked, button)
    #         button.grid(row=row, column=col)
    #         Game_Board.btns.append(button)
    #         Game_Board.btns[row][col] = button

    def button_obj(self, location):
        Game_Board.btns = [[None] * 20 for _ in range(20)]
        for i in range(20):
            for j in range(20):
                button = Button(location,
                                width=3,
                                height=1,
                                state="disabled",
                                text=''
                                )
                # callback, which also submits the button innstance to the function
                button["command"] = partial(self.clicked, button)
                button.grid(row=i, column=j)
                Game_Board.btns[i][j] = button

    # def button_obj(self, location):
    #     for x in range(settings.GRID_SIZE):
    #         for y in range(settings.GRID_SIZE):
    #             c1 = Cell(x, y)
    #             c1.create_btn_object(location)
    #             c1.cell_btn_object.grid(
    #                 column=y, row=x
    #             )

    def clicked(self, button: Button):
        row = button.grid_info()['row']
        col = button.grid_info()['column']
        txt = f'({row}, {col})'
        Cell.cell_click(row, col)
        # print(Game_Board.btns[row][col])
        self.view.update_text_contents(txt)


# Create the root window
root = tk.Tk()

# Create the controller
controller = Controller(root)

Cell.set_players()

# Start the Tkinter event loop
root.mainloop()
