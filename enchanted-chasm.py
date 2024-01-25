'''
Program Name: enchanted-chasm.py
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
- Build a list where there is a wall
* Define obstales in a dictionary
* Place monster, pit, treasure on the board
* Generate random spawn locations
* Move the hero


'''
import random

#user_wall_choice = int(input('Enter the number of walls needed: '))
user_wall_choice = 1
MASTER_OBSTACLES = {'W':[], 'M':[], 'H':[], 'T':[], 'P':[]}
MASTER_BOARD = []
MASTER_OBSTACLE_LOCATIONS = []
MASTER_SPAWN_LOCATIONS = []
DEBUG_SPAWN_LOCATIONS = []

# Build NxN Wall 
def game_board (row, col) :
    #my_wall = []

    i = 0
    while i < row:
        # Initialize the inner list for each row
        MASTER_BOARD.append([])

        j = 0
        while j < col:
            # 
            if (j == 0) or (j == col - 1) or (i == 0) or (i == row - 1):
                MASTER_BOARD[i].append('W')
            else:
                MASTER_BOARD[i].append('E')
            j += 1

        i += 1
    return MASTER_BOARD

# Store a list of locations where a wall is
def obstacle_locations (wall) :
    #my_list = []
    rows = len(wall)
    i = 0
    while i < rows:
        # 
        MASTER_OBSTACLE_LOCATIONS.append([])
        cols = len(wall[i])
        j = 0
        while j < cols:
            if (wall[i][j] == 'W') or (wall[i][j] == 'P') or (wall[i][j] == 'T') or (wall[i][j] == 'M') or (wall[i][j] == ' '):
                MASTER_OBSTACLE_LOCATIONS[i].append(j)
            j += 1
        i += 1
    return MASTER_OBSTACLE_LOCATIONS

# Catalog empty locations
def spawn_locations (wall) :
    #my_list = []
    rows = len(wall)
    i = 0
    while i < rows:
        #
        MASTER_SPAWN_LOCATIONS.append([])
        cols = len(wall[i])
        j = 0
        while j < cols:
            if (wall[i][j] == 'E') :
                MASTER_SPAWN_LOCATIONS[i].append(j)
            j += 1
        i += 1
    return MASTER_SPAWN_LOCATIONS

# Debug, clean view, to show where the obstacles are
def debug_spawn_locations (wall) :
    # NEED TO FIX
    #my_list = []
    rows = len(wall)
    i = 0
    while i < rows:
        #
        DEBUG_SPAWN_LOCATIONS.append([])
        cols = len(wall[i])
        j = 0
        while j < cols:
            if (wall[i][j] == 'E') :
                DEBUG_SPAWN_LOCATIONS[i].append('')
            else :
                DEBUG_SPAWN_LOCATIONS[i].append(wall[i][j])
            j += 1
        i += 1
    return DEBUG_SPAWN_LOCATIONS

def initialize_obstacle_location (board) :
    obstacles_list = ['W','P','T', 'M']
    rows = len(board) - 1
    cols = len(board[0]) - 1

    # MASTER_OBSTACLES.update({'H' : [ran_row, ran_col]})

    i = 0 
    while i < len(obstacles_list) :
        ran_row = random.sample(range(1, rows), 1)[0]
        ran_col = random.sample(range(1, cols), 1)[0]
        # Enforce the rules for obstacle locations
        MASTER_OBSTACLES.update({obstacles_list[i] : [ran_row, ran_col]})

        MASTER_BOARD[ran_row][ran_col] = obstacles_list[i]
        
        i += 1

    
    return MASTER_OBSTACLES

def spawn_hero () :
    heros_list = ['H']
    rows = len(MASTER_SPAWN_LOCATIONS) - 1
    cols = len(MASTER_SPAWN_LOCATIONS[0]) - 1

    # MASTER_OBSTACLES.update({'H' : [ran_row, ran_col]})

    i = 0
    while i < len(heros_list):
        ran_row = random.sample(range(1, rows), 1)[0]

        ran_col = random.choice(MASTER_SPAWN_LOCATIONS[ran_row])
        #ran_col = random.sample(range(1, cols), 1)[0]
        # Enforce the rules for obstacle locations
        MASTER_OBSTACLES.update({heros_list[i]: [ran_row, ran_col]})

        MASTER_BOARD[ran_row][ran_col] = heros_list[i]

        i += 1

    return MASTER_OBSTACLES


# Initialize the game
def initialze_board () :
    game_board(20, 20)
    initialize_obstacle_location(MASTER_BOARD)
    obstacle_locations(MASTER_BOARD)
    spawn_locations(MASTER_BOARD)
    debug_spawn_locations(MASTER_BOARD)
    return MASTER_BOARD

initialze_board()

# Creats a list of locations where there is a wall per row















