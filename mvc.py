import tkinter as tk
from tkinter import ttk, Button
from itertools import product
from functools import partial
from Class.cell import Cell
from Class.board import Game_Board
from Utilities import settings

class Model:
    def __init__(self):
        self.text_contents = ""

    def set_text_contents(self, new_contents):
        self.text_contents = new_contents

    Game_Board.init_board('GameBoard/TheCave.txt')
    Game_Board.obstacle_locations()
    Game_Board.spawn_object('H')
    Game_Board.button_locations()

class View:
    def __init__(self, root, controller):
        self.root = root
        self.controller = controller

        # create window for grids
        root.title('The Enchanted Chasm')
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
        self.text_widget.insert("1.0", 'Lets get ready to rumble!\nStart selecting buttons to find your treasure!' + "\n")

    def update_text_contents(self, new_contents):
        # Update the Text widget with the new text contents
        # self.text_widget.delete("1.0", tk.END)
        self.text_widget.insert("1.0", new_contents + "\n")

class Controller:
    def __init__(self, root):
        self.root = root
        self.model = Model()
        self.view = View(root, self)

    def set_text_contents(self):
        new_contents = 'new text'  # Define the new contents of the Text widget
        self.model.set_text_contents(new_contents)  # Update the model with the new contents
        self.view.update_text_contents(new_contents)  # Update the view with the new contents

    def button_obj(self, location):
        Game_Board.btns = [[None] * settings.GRID_SIZE for _ in range(settings.GRID_SIZE)]
        for i in range(settings.GRID_SIZE):
            for j in range(settings.GRID_SIZE):
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

    def clicked(self, button: Button):
        row = button.grid_info()['row']
        col = button.grid_info()['column']
        Cell.cell_click(row, col)
        if Cell.log_obs() != None:
            self.view.update_text_contents(Cell.log_obs())

# Create the root window
root = tk.Tk()

# Create the controller
controller = Controller(root)

Cell.set_players()


# Start the Tkinter event loop
root.mainloop()
