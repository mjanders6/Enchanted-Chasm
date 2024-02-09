'''
Program Name: enchanted-chasm.py
Github Repository: https://github.com/mjanders6/Enchanted-Chasm
Author: Michael J. Anderson
Date: 24JanFeb2024


Purpose:
Build a one-row Cave complete with one Pit, Monster, and Treasure. Include the placement of the Hero and Walls.


Customer Requirements:

The Cave (20x1 squares) must contain the following: Hero, Walls, Pit, Monster, and Treasure
- At a minimum, Walls must be located at the ends (0,0) and (20,0)
- The number of walls must be obtained by the user (at least three(3)… the ends and at least one interior)
- The Monster must not be placed within three(3) squares of the Treasure and Pit
- The Pit must not be placed within two(2) squares from the Treasure
- The Hero must not be placed a.) within three(3) squares from the Monster and b.) within two(2) squares from the Pit and Treasure

- Hero, Treasure, Pit, and Monster cannot be placed within a Wall

Pseudo Code
    Build the board
    Build  the interrior walls
    Load the walls into the board
    Create a list of locations on where the walls are
    Define obstacle locations within a dictionary
        compare dictioary values to ensure
            Nothing is within a wall
            The Monster must not be placed within three(3) squares of the Treasure and Pit
            The Pit must not be placed within two(2) squares from the Treasure
            The Hero must not be placed a.) within three(3) squares from the Monster and b.) within two(2) squares from the Pit and Treasure


List of Functions:
- Generate board
* Generate interior walls
- Build a list where there is an obstacles and walls
* Place monster, pit, treasure on the board
* Generate random spawn locations
* Move the hero


'''
import random
import os
import sys
sys.path.append(os.path.realpath("."))
import inquirer
from inquirer.themes import GreenPassion
from tkinter import *
from Class.cell import Cell
from Class.board import Game_Board
from Utilities import settings, utils

file = "GameBoard/TheCave.txt"

master_board = Game_Board()

def obstacle_check(object, chk_obj):
    #  Update Cell.MASTER_OBSTACLES to reflect the different relationships
    lstKeys = list(master_board.MASTER_OBSTACLES.keys())
    master_board.OBSTACLE_CHECK_LIST.clear()
    # Constant for N spaces from obstacle being compared
    k_obs = 2
    # Calculate upper and lower bounds to check if an obstacle is N spaces close
    r = master_board.MASTER_OBSTACLES[object][0]
    c = master_board.MASTER_OBSTACLES[object][1]
    r_l = master_board.MASTER_OBSTACLES[object][0] - k_obs
    c_l = master_board.MASTER_OBSTACLES[object][1] - k_obs
    r_upper_bound = master_board.MASTER_OBSTACLES[object][0] + k_obs
    c_upper_bound = master_board.MASTER_OBSTACLES[object][1] + k_obs

    while r_l <= r_upper_bound and r_l != object:
        if r_l < 0 or r_l >= 20:
            master_board.OBSTACLE_CHECK_LIST.update({'O':[r_l, c]})
        else:
            master_board.OBSTACLE_CHECK_LIST.update({Cell.MASTER_BOARD[r_l][c]:[r_l,c]})
        while c_l <= c_upper_bound and c_l != object:
            if c_l <  0 or c_l >= 20:
                master_board.OBSTACLE_CHECK_LIST.update({'O': [r, c_l]})
            else:
                master_board.OBSTACLE_CHECK_LIST.update({Cell.MASTER_BOARD[r][c_l]:[r, c_l]})
            c_l += 1
        r_l += 1

    if chk_obj in master_board.OBSTACLE_CHECK_LIST:
        #print(f'Collision detected')
        return 1
    else:
        #print(f'No Collision Detected')
        return 0

# Initialize the hero on the board
def initialize_hero_location ():
    Game_Board.spawn_object('H')

def game_gui():

    root = Tk()
    # override window settings
    root.configure(bg='gray')
    root.geometry(f'{settings.WIDTH}x{settings.HEIGHT}')
    root.title('Enchanted Chasm')
    root.resizable(False, False)

    top_frame = Frame(
        root,
        bg='gray',
        width=settings.WIDTH,
        height=utils.height_prct(25)
    )
    top_frame.place(x=0, y=0)

    left_frame = Frame(
        root,
        bg='gray',
        width=utils.width_prct(25),
        height=utils.height_prct(75)
    )
    left_frame.place(x=0, y=utils.height_prct(25))

    center_frame = Frame(
        root,
        bg='white',
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
                column=y, row=x
            )

    Cell.set_players()

    root.mainloop()

# Initialize the game
def game_start():
    game_board()
    spawn_object('H')
    obstacle_locations()
    Cell.spawn_locations()
    debug_spawn_locations()
    for i in Cell.MASTER_BOARD:
        print(i)

def show_board():
    # for i in Cell.MASTER_BOARD:
    #     print(i)
    rows = len(Cell.MASTER_BOARD)
    board = []
    i = 0
    while i < rows:
        #
        board.append([])
        cols = len(Cell.MASTER_BOARD[i])
        j = 0
        while j < cols:
            if (Cell.MASTER_BOARD[i][j] != 'H') :
                board[i].append(' ')
            else :
                board[i].append(Cell.MASTER_BOARD[i][j])
            j += 1
        i += 1
    for i in board:
        print(' '.join(i))

def cheat_board():
    for i in master_board.DEBUG_SPAWN_LOCATIONS:
        print(' '.join(i))

def game_mode():
    q_continue = [inquirer.List("continue", message="Are you ready for an adventure of a lifetime? Choose your next move",
                                choices=['Start Game', 'Quit while your ahead'], default="Start Game")]
    q_next_move = [inquirer.List("next_move", message="Choose your next move",
                                 choices=['Move', 'Cheat', 'Quit'], default="Move")]

    while True:
        answers = inquirer.prompt(q_continue, theme=GreenPassion())
        if answers['continue'] == 'Start Game':
            game_start()
            next_move = inquirer.prompt(q_next_move, theme=GreenPassion())
            if next_move['next_move'] == 'Move':
                print('this is where you would move')
            elif next_move['next_move'] == 'Cheat':
                show_board()
            elif next_move['next_move'] == 'Quit':
                print('Thank you for your bravery!')
                break

        if answers['continue'] == 'Quit while your ahead':
            break

# Explore the Chasm

def main():
    #game_mode()
    master_board.init_board(file)
    master_board.spawn_locations()
    master_board.button_locations()
    initialize_hero_location()
    cheat_board()
    game_gui()


if __name__ == "__main__":
    main()
