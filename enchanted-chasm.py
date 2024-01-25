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
    my_wall = []

    i = 0
    while i < row:
        # Initialize the inner list for each row
        my_wall.append([])

        j = 0
        while j < col:
            # 
            if (j == 0) or (j == col - 1) or (i == 0) or (i == row - 1):
                my_wall[i].append('W')
            else:
                my_wall[i].append('E')
            j += 1

        i += 1
    return my_wall

# Store a list of locations where a wall is
def obstacle_locations (wall) :
    my_list = []
    rows = len(wall)
    i = 0
    while i < rows:
        # 
        my_list.append([])
        cols = len(wall[i])
        j = 0
        while j < cols:
            if (wall[i][j] == 'W') or (wall[i][j] == 'P') or (wall[i][j] == 'T') or (wall[i][j] == 'M') or (wall[i][j] == ' '):
                my_list[i].append(j)
            j += 1
        i += 1
    return my_list

def spawn_locations (wall) :
    my_list = []
    rows = len(wall)
    i = 0
    while i < rows:
        #
        my_list.append([])
        cols = len(wall[i])
        j = 0
        while j < cols:
            if (wall[i][j] == 'E') :
                my_list[i].append(j)
            j += 1
        i += 1
    return my_list

def debug_spawn_locations (wall) :
    my_list = []
    rows = len(wall)
    i = 0
    while i < rows:
        #
        my_list.append([])
        cols = len(wall[i])
        j = 0
        while j < cols:
            if (wall[i][j] == 'E') :
                my_list[i].append('')
            else :
                my_list[i].append(wall[i][j])
            j += 1
        i += 1
    return my_list

def initialize_obstacle_location (board) :
    obstacles_list = ['W','P','T', 'M']
    rows = len(board) - 1
    cols = len(board[0]) - 1

    # MASTER_OBSTACLES.update({'H' : [ran_row, ran_col]})

    i = 0 
    while i < len(obstacles_list) :
        ran_row = random.sample(range(1, rows), 1)[0]
        ran_col = random.sample(range(1, cols), 1)[0]

        MASTER_OBSTACLES.update({obstacles_list[i] : [ran_row, ran_col]})

        MASTER_BOARD[ran_row][ran_col] = obstacles_list[i]
        
        i += 1

    
    return MASTER_OBSTACLES


def set_obstacles (wall) :
    obstacles_list = ['W','P','T','H', 'M']
    obs_locations = {'W':[], 'P':[], 'H':[], 'T':[], 'P':[]}
    rows = len(wall)
    cols = len(wall[0]) - 1

    i = 0
    while i < len(obstacles_list) :
        # create first set of random numbers for the row and column
        ran_row_sample = random.sample(range(1, rows), 1)[0]
        ran_col_sample = random.sample(range(1, cols), 1)[0]

        # If the random row row and column fall on a wall, generate a new row and column
        if wall[ran_row_sample][ran_col_sample] == 'W' :
            ran_row_sample_loop = random.sample(range(1, rows), 1)[0]
            ran_col_sample_loop = random.sample(range(1, cols), 1)[0]
            # Change the value to the obstacle: W, H, T, P, or M
            wall[ran_row_sample_loop][ran_col_sample_loop] = obstacles_list[i]
            # Store the obstacle location in a dictionary to validaye obstacle constraints
            obs_locations.update({obstacles_list[i] : [ran_row_sample_loop, ran_col_sample_loop]})

            # Obstacle constraints
            
            
        else :
            # If the row and column do not fall on a Wall
            # Change the value to the obstacle: W, H, T, P, or M
            wall[ran_row_sample][ran_col_sample] = obstacles_list[i]
            # Store the obstacle location in a dictionary to validaye obstacle constraints
            obs_locations.update({obstacles_list[i] : [ran_row_sample, ran_col_sample]})
        i += 1

    print(obs_locations)
    return [wall, obs_locations]

###############

# Function to find the location where the pit, monster,and treasure are

# Generate random locations

# Sets an NxN wall
MASTER_BOARD = game_board(20, 20)

initialize_obstacle_location(MASTER_BOARD)

# Creats a list of locations where there is a wall per row
MASTER_OBSTACLE_LOCATIONS = obstacle_locations(MASTER_BOARD)
MASTER_SPAWN_LOCATIONS = spawn_locations(MASTER_BOARD)
DEBUG_SPAWN_LOCATIONS = debug_spawn_locations(MASTER_BOARD)














