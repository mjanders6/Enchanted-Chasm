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
from pprint import pprint
sys.path.append(os.path.realpath("."))
import inquirer
from inquirer.themes import GreenPassion
import PySimpleGUI as sg

# Build NxN Wall 
def game_board () :
    file_path = "TheCave.txt"
    with open(file_path, 'r') as file:
        # Iterate over each line in the file
        for line in file:
            # Split the line into fields based on whitespace
            fields = line.strip().split()
            MASTER_BOARD.append(fields)
    # i = 0
    # while i < row:
    #     # Initialize the inner list for each row
    #     MASTER_BOARD.append([])
    #     #MASTER_BOARD_LIST.append([])
    #
    #     j = 0
    #     while j < col:
    #
    #         if (j == 0) or (j == col - 1) or (i == 0) or (i == row - 1):
    #             MASTER_BOARD[i].append('W')
    #             #MASTER_BOARD_LIST[i].append([i, j])
    #         else:
    #             MASTER_BOARD[i].append('E')
    #             #MASTER_BOARD_LIST[i].append([i, j])
    #         j += 1
    #
    #     i += 1
    return MASTER_BOARD

def obstacle_check(object, chk_obj):
    #  Update MASTER_OBSTACLES to reflect the different relationships
    lstKeys = list(MASTER_OBSTACLES.keys())
    OBSTACLE_CHECK_LIST.clear()
    # Constant for N spaces from obstacle being compared
    k_obs = 2
    # Calculate upper and lower bounds to check if an obstacle is N spaces close
    r = MASTER_OBSTACLES[object][0]
    c = MASTER_OBSTACLES[object][1]
    r_l = MASTER_OBSTACLES[object][0] - k_obs
    c_l = MASTER_OBSTACLES[object][1] - k_obs
    r_upper_bound = MASTER_OBSTACLES[object][0] + k_obs
    c_upper_bound = MASTER_OBSTACLES[object][1] + k_obs

    while r_l <= r_upper_bound and r_l != object:
        if r_l < 0 or r_l >= 20:
            OBSTACLE_CHECK_LIST.update({'O':[r_l, c]})
        else:
            OBSTACLE_CHECK_LIST.update({MASTER_BOARD[r_l][c]:[r_l,c]})
        while c_l <= c_upper_bound and c_l != object:
            if c_l <  0 or c_l >= 20:
                OBSTACLE_CHECK_LIST.update({'O': [r, c_l]})
            else:
                OBSTACLE_CHECK_LIST.update({MASTER_BOARD[r][c_l]:[r, c_l]})
            c_l += 1
        r_l += 1

    if chk_obj in OBSTACLE_CHECK_LIST:
        #print(f'Collision detected')
        return 1
    else:
        #print(f'No Collision Detected')
        return 0

# Store a list of locations where a location is not blank
def obstacle_locations () :
    OBSTACLE_LOCATIONS.clear()
    MASTER_OBSTACLE_LOCATIONS.clear()
    rows = len(MASTER_BOARD)
    i = 0
    while i < rows:
        # 
        OBSTACLE_LOCATIONS.append([])
        MASTER_OBSTACLE_LOCATIONS.append([])
        cols = len(MASTER_BOARD[i])
        j = 0
        while j < cols:
            if (MASTER_BOARD[i][j] == 'W') or (MASTER_BOARD[i][j] == 'P') or (MASTER_BOARD[i][j] == 'H') or (MASTER_BOARD[i][j] == 'T') or (MASTER_BOARD[i][j] == 'M') or (MASTER_BOARD[i][j] == ' '):
                OBSTACLE_LOCATIONS[i].append(j)
                MASTER_OBSTACLE_LOCATIONS.append([i, j])
                if MASTER_BOARD[i][j] != 'W':
                    MASTER_OBSTACLES.update({ MASTER_BOARD[i][j] : [i, j]})
            j += 1
        i += 1
    return OBSTACLE_LOCATIONS

# Catalog empty locations
def spawn_locations () :
    SPAWN_LOCATIONS.clear()
    MASTER_SPAWN_LOCATIONS.clear()
    rows = len(MASTER_BOARD)
    i = 0
    while i < rows:
        #
        SPAWN_LOCATIONS.append([])
        MASTER_SPAWN_LOCATIONS.append([])
        cols = len(MASTER_BOARD[i])
        j = 0
        while j < cols:
            if (MASTER_BOARD[i][j] == 'E') :
                SPAWN_LOCATIONS[i].append(j)
                MASTER_SPAWN_LOCATIONS.append([i, j])
            j += 1
        i += 1
    return SPAWN_LOCATIONS

# Debug, clean view, to show where the obstacles are
def debug_spawn_locations () :
    DEBUG_SPAWN_LOCATIONS.clear()
    rows = len(MASTER_BOARD)

    i = 0
    while i < rows:
        #
        DEBUG_SPAWN_LOCATIONS.append([])
        cols = len(MASTER_BOARD[i])
        j = 0
        while j < cols:
            if (MASTER_BOARD[i][j] == 'E') :
                DEBUG_SPAWN_LOCATIONS[i].append(' ')
            else :
                DEBUG_SPAWN_LOCATIONS[i].append(MASTER_BOARD[i][j])
            j += 1
        i += 1
    return DEBUG_SPAWN_LOCATIONS

# Initialize the board with obstacles
def initialize_obstacle_location () :
    # initialize obstacles list
    # initialize # of row/# of column
    # initiate first obstacle
    # create location for next object from list of spawnable locations
        # If M -> threshhold is 3
        # If not M -> threshhold is 2

    obj_list = ['P', 'M', 'H']

    # The number of walls must be obtained by the user (at least three(3)… the ends and at least one interior)
    user_input = 1  # input(f'Are you ready to exploire?\nResponse:\n1. Y\n2. N')

    # The Monster must not be placed within three(3) squares of the Treasure and Pit
    spawn_object('T')

    for i in obj_list:
        spawn_object(i)
        while obstacle_check('T', i) == 1:
            print(i , OBSTACLE_CHECK_LIST)
            #MASTER_BOARD.remove[:] = [value for value in MASTER_BOARD.remove if value != i]
            for index, value in enumerate(MASTER_BOARD):
                if i == value:
                    MASTER_BOARD[index] = 'E'

            spawn_object(i)
            print('spawn again')

# Initialize the hero on the board
def initialize_hero_location () :
    # initialize obstacles list
    # initialize # of row/# of column
    # initiate first obstacle
    # create location for next object from list of spawnable locations
        # If M -> threshhold is 3
        # If not M -> threshhold is 2

    obj_list = ['P', 'M', 'T']

    # The number of walls must be obtained by the user (at least three(3)… the ends and at least one interior)
    user_input = 1  # input(f'Are you ready to exploire?\nResponse:\n1. Y\n2. N')

    # The Monster must not be placed within three(3) squares of the Treasure and Pit
    spawn_object('H')

    # for i in obj_list:
    #     while obstacle_check('H', i) == 1:
    #         print(i , OBSTACLE_CHECK_LIST)
    #         #MASTER_BOARD.remove[:] = [value for value in MASTER_BOARD.remove if value != i]
    #         for index, value in enumerate(MASTER_BOARD):
    #             if i == value:
    #                 MASTER_BOARD[index] = 'E'
    #
    #         spawn_object(i)
    #         print('spawn again')

def spawn_wall(object, num_walls) :
    spawn_locations()
    rows = len(SPAWN_LOCATIONS) - 1

    wall_num = 0
    while wall_num < num_walls:
        ran_row = random.sample(range(1, rows), 1)[0]
        ran_col = random.choice(SPAWN_LOCATIONS[ran_row])
        # place W on the board
        MASTER_BOARD[ran_row][ran_col] = object
        wall_num += 1
    # Update tables
    obstacle_locations()
    debug_spawn_locations()
    spawn_locations()

# Spawn an object H, M, W, T, P
def spawn_object (object) :
    spawn_locations()
    rows = len(SPAWN_LOCATIONS) - 1

    ran_row = random.sample(range(1, rows), 1)[0]
    ran_col = random.choice(SPAWN_LOCATIONS[ran_row])
    # Check to see if location is not within a certain amount of spaces
    MASTER_OBSTACLES.update({ object : [ran_row, ran_col]})
    MASTER_BOARD[ran_row][ran_col] = object

    obstacle_locations()
    debug_spawn_locations()
    spawn_locations()

# def button1(text, key=None, disabled=False, button_color=('white', 'green')):
#     return sg.Button(text, pad=(10, 10), font=font, focus=False, key=key,
#             disabled=disabled, button_color=button_color)

def game_gui():
    rows = len(MASTER_BOARD)
    board = []
    i = 0
    while i < rows:
        #
        board.append([])
        cols = len(MASTER_BOARD[i])
        j = 0
        while j < cols:
            if (MASTER_BOARD[i][j] != 'H' and MASTER_BOARD[i][j] != 'M' and MASTER_BOARD[i][j] != 'T' and MASTER_BOARD[i][j] != 'P' and MASTER_BOARD[i][j] != 'W'):
                # board[i].append(ReadFormButton(''))
                board[i].append(sg.Button('', key=(i, j), size=(3, 1), visible = True, disabled = True))
            else:
                # board[i].append(ReadFormButton(MASTER_BOARD[i][j]))
                board[i].append(sg.Button(MASTER_BOARD[i][j], key=(i,j), button_color=("white", "blue"), size=(3, 1), visible = True, disabled = False))
            j += 1
        i += 1
    col1 = sg.Column([[sg.Frame('Interaction:', [[sg.Column([[]], size=(450, 225), pad=(15, 0))]])]], pad=(0, 0))

    col2 = sg.Column([[sg.Frame('Chasm:', board, expand_x=True, expand_y=True)]], element_justification='c',size=(450, 450), expand_x=True, expand_y=True, pad=(0, 0))

    # window = sg.Window("Mass File Transfer").Layout(board)

    layout = [[sg.vtop(col1), sg.VSeperator(), col2]]
    window = sg.Window('Columns and Frames', layout, size=(1500, 950), grab_anywhere=True, resizable=True,margins=(0, 0))

    while True:
        event, values = window.Read()
        print(event, window[event].get_text())

        if event in (None, 'Exit'):
            break



# Initialize the game
def game_start():
    # q = [
    #     inquirer.List("start", message="Are you ready for an adventure of a lifetime?", choices=["Yes", "No"], default="Yes")
    # ]
    # answers = inquirer.prompt(q, theme=GreenPassion())
    #
    # if answers['start'] == 'Yes':
    game_board()
    initialize_hero_location()
    obstacle_locations()
    spawn_locations()
    debug_spawn_locations()
    for i in MASTER_BOARD:
        print(i)

def show_board():
    # for i in MASTER_BOARD:
    #     print(i)
    rows = len(MASTER_BOARD)
    board = []
    i = 0
    while i < rows:
        #
        board.append([])
        cols = len(MASTER_BOARD[i])
        j = 0
        while j < cols:
            if (MASTER_BOARD[i][j] != 'H') :
                board[i].append(' ')
            else :
                board[i].append(MASTER_BOARD[i][j])
            j += 1
        i += 1
    for i in board:
        print(' '.join(i))

def cheat_board():
    for i in DEBUG_SPAWN_LOCATIONS:
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



#where list1 = [[x, y]]
'''def colission(list1, list2):
    for x,y in enumerate(list1):
        for a,b in enumerate(list2):
            if x == a and y == b:
                print('found wall')
'''


# Explore the Chasm

def main():
    # game_mode()
    game_board()
    initialize_hero_location()
    obstacle_locations()
    spawn_locations()
    debug_spawn_locations()



if __name__ == "__main__":
    MASTER_OBSTACLES = {'T':[], 'M':[], 'H':[], 'P':[]}
    MASTER_BOARD = []
    MASTER_BOARD_LIST = []
    OBSTACLE_LOCATIONS = []
    SPAWN_LOCATIONS = []
    DEBUG_SPAWN_LOCATIONS = []
    HISTORICAL_MOVEMENTS = []
    OBSTACLE_CHECK_LIST = {}

    # Used to compare a list of tuples
    MASTER_OBSTACLE_LOCATIONS = []
    MASTER_SPAWN_LOCATIONS = []

    # Used to compare a list of tuples
    MASTER_OBSTACLE_LOCATIONS = []
    MASTER_SPAWN_LOCATIONS = []
    main()