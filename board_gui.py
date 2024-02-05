from tkinter import *
from cell import Cell
import settings
import utils



root = Tk()
# override window settings
root.configure(bg='gray')
root.geometry(f'{settings.WIDTH}x{settings.HEIGHT}')
root.title('Enchanted Chasm')
root.resizable(False, False)

top_frame = Frame(
    root,
    bg = 'gray',
    width=settings.WIDTH,
    height=utils.height_prct(25)
)
top_frame.place(x=0, y=0)

left_frame = Frame(
    root,
    bg = 'gray',
    width=utils.width_prct(25),
    height=utils.height_prct(75)
)
left_frame.place(x=0, y=utils.height_prct(25))

center_frame = Frame(
    root,
    bg = 'white',
    width=utils.width_prct(75),
    height=utils.height_prct(75)
)
center_frame.place(
    x=utils.width_prct(25),
    y=utils.height_prct(25))


for x in range(settings.GRID_SIZE):
    for y in range(settings.GRID_SIZE):
        c1 = Cell(x, y)
        c1.create_btn_object(center_frame)
        c1.cell_btn_object.grid(
            column=x, row=y
        )

Cell.randomize_mines()

# Notes from different buttons placements
# c2 = Cell()
# c2.create_btn_object(center_frame)
# c2.cell_btn_object.place(
#     x=1, y=0
# )
# c2 = Cell()
# c2.create_btn_object(center_frame)
# c2.cell_btn_object.grid(
#     column=1, row=0
# )
# btn1 = Button(
#     center_frame,
#     bg='blue',
#     text='First BTN'
# )
# btn1.place(x=0, y=0)

# run the windeo
root.mainloop()
