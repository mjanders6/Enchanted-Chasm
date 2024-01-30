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
    Build the interior wall
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
NUM_WALLS = 1 # for debugging
MASTER_OBSTACLES = {'T':0, 'M':0, 'H':0, 'P':0}
MASTER_BOARD = []
OBSTACLE_LOCATIONS = []
SPAWN_LOCATIONS = []
DEBUG_SPAWN_LOCATIONS = []
HISTORICAL_MOVEMENTS = []
OBSTACLE_CHECK_LIST = {'T':0, 'M':0, 'H':0, 'P':0}

# Used to compare a list of tuples
MASTER_OBSTACLE_LOCATIONS = []
MASTER_SPAWN_LOCATIONS = []

# Build NxN Wall
def game_board (col) :
    j = 0
    while j < col:
        #
        if (j == 0) or (j == col - 1):
            MASTER_BOARD.append('W')
        else:
            MASTER_BOARD.append('E')
        j += 1

    return MASTER_BOARD

# Store a list of locations where a location is not blank
def obstacle_locations () :
    OBSTACLE_LOCATIONS.clear()
    MASTER_OBSTACLE_LOCATIONS.clear()
    #
    cols = len(MASTER_BOARD)
    j = 0
    while j < cols:
        if (MASTER_BOARD[j] == 'W') or (MASTER_BOARD[j] == 'P') or (MASTER_BOARD[j] == 'H') or (MASTER_BOARD[j] == 'T') or (MASTER_BOARD[j] == 'M') or (MASTER_BOARD[j] == ' '):
            OBSTACLE_LOCATIONS.append(j)
            MASTER_OBSTACLE_LOCATIONS.append([(j)])
        j += 1

    return OBSTACLE_LOCATIONS

# Catalog empty locations
def spawn_locations () :
    SPAWN_LOCATIONS.clear()
    MASTER_SPAWN_LOCATIONS.clear()
    cols = len(MASTER_BOARD)
    j = 0
    while j < cols:
        if (MASTER_BOARD[j] == 'E') :
            SPAWN_LOCATIONS.append(j)
            MASTER_SPAWN_LOCATIONS.append([(j)])
        j += 1

    return SPAWN_LOCATIONS

# Debug, clean view, to show where the obstacles are
def debug_spawn_locations () :
    DEBUG_SPAWN_LOCATIONS.clear()
    rows = len(MASTER_BOARD)

    if len(DEBUG_SPAWN_LOCATIONS) > 0:

        cols = len(MASTER_BOARD)
        j = 0
        while j < cols:
            if (MASTER_BOARD[j] == 'E') :
                DEBUG_SPAWN_LOCATIONS.append('')
            else :
                DEBUG_SPAWN_LOCATIONS.append(MASTER_BOARD[j])
            j += 1

    else:
        cols = len(MASTER_BOARD)
        j = 0
        while j < cols:
            if (MASTER_BOARD[j] == 'E') :
                DEBUG_SPAWN_LOCATIONS.append('')
            else :
                DEBUG_SPAWN_LOCATIONS.append(MASTER_BOARD[j])
            j += 1


    return DEBUG_SPAWN_LOCATIONS

# Check
def obstacle_check(object):
    #  Update MASTER_OBSTACLES to reflect the different relationships
    lstKeys = list(MASTER_OBSTACLES.keys())
    OBSTACLE_CHECK_LIST.clear()
    # Constant for N spaces from obstacle being compared
    if object == 'M':
        k_obs = 3
    else:
        k_obs = 2
    # Calculate upper and lower bounds to check if an obstacle is N spaces close
    c = MASTER_OBSTACLES[object]
    c_l = MASTER_OBSTACLES[object] - k_obs
    c_upper_bound = MASTER_OBSTACLES[object] + k_obs

    while c_l <= c_upper_bound:
        if c_l >= 0 and c_l < 20 and DEBUG_SPAWN_LOCATIONS[c_l] != object and DEBUG_SPAWN_LOCATIONS[c_l] != '' and DEBUG_SPAWN_LOCATIONS[c_l] != 'W':
            #print(DEBUG_SPAWN_LOCATIONS[r][c_l])
            OBSTACLE_CHECK_LIST.update({DEBUG_SPAWN_LOCATIONS[c_l]: c_l})
        c_l += 1


    #print(f'{object} | {OBSTACLE_CHECK_LIST}')

    for key, value in OBSTACLE_CHECK_LIST.items():
        while abs(value - c) < k_obs:
            return 1

    '''for key, value in OBSTACLE_CHECK_LIST.items():
        if key == 'P' or key == 'T' or key == 'H' and  key == 'M':
            while abs(value - c) < k_obs:
                return 1
            if key == 'P' or key == 'T' and key == 'M':
                while abs(value - c) < k_obs:
                    return 1
                if key == 'P' or key == 'T':
                    while abs(value - c) < k_obs:
                        return 1
                    if key == 'P':
                        while abs(value - c) < k_obs:
                            return 1'''


# Initialize the board with obstacles
def initialize_obstacle_location () :
    global DEBUG_SPAWN_LOCATIONS
    # Initialize variables
    obj_list = ['P', 'M', 'H']
    spaces = 2
    # The number of walls must be obtained by the user (at least three(3)… the ends and at least one interior)
    user_input = 1  # input(f'Are you ready to exploire?\nResponse:\n1. Y\n2. N')
    spawn_wall('W')
    # The Monster must not be placed within three(3) squares of the Treasure and Pit
    spawn_object('T')

    for i in obj_list:
        spawn_object(i)
        while obstacle_check(i) == 1:
            print(i , OBSTACLE_CHECK_LIST)
            DEBUG_SPAWN_LOCATIONS[:] = [value for value in DEBUG_SPAWN_LOCATIONS if value not in i]

            spawn_object(i)
            print('spawn again')





    # The Pit must not be placed within two(2) squares from the Treasure

    # The Hero must not be placed a.) within three(3) squares from the Monster and b.) within two(2) squares from the Pit and Treasure

    # Hero, Treasure, Pit, and Monster cannot be placed within a Wall

# Spawn a wall
def spawn_wall(object) :
    spawn_locations()

    ran_col = random.choice(SPAWN_LOCATIONS)
    # place W on the board
    MASTER_BOARD[ran_col] = object

    # Update tables
    obstacle_locations()
    debug_spawn_locations()
    spawn_locations()

# Spawn an object H, M, W, T, P
def spawn_object (object) :
    spawn_locations()
    rows = len(SPAWN_LOCATIONS) - 1

    ran_col = random.choice(SPAWN_LOCATIONS)
    # Check to see if location is not within a certain amount of spaces
    MASTER_OBSTACLES.update({ object : ran_col})
    MASTER_BOARD[ran_col] = object

    obstacle_locations()
    debug_spawn_locations()
    spawn_locations()

# Initialize the game
def initialze_board () :
    game_board(20)
    initialize_obstacle_location()
    obstacle_locations()
    spawn_locations()
    debug_spawn_locations()

initialze_board()

'''
# Explore the Chasm
USER_INPUT = input(f'Are you ready to exploire?\nResponse:\n1. Y\n2. N')


while USER_INPUT != 'N' or USER_INPUT != 'n':
    if (USER_INPUT == 'Y' or USER_INPUT == 'y') :
        NUM_WALLS = int(input(f'How many walls do you want to add?\nResponse:  '))
        while NUM_WALLS >= 14:
            NUM_WALLS = int(input(f'You entered {NUM_WALLS}. Number must be less than 14. \nResponse:  '))
        else :
            initialze_board()
    break
'''





