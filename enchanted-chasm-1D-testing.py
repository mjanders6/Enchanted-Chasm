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
# NUM_WALLS = 1 # for debugging
MASTER_OBSTACLES = {'T':0, 'M':0, 'H':0, 'P':0}
MASTER_BOARD = []
OBSTACLE_LOCATIONS = []
SPAWN_LOCATIONS = []
DEBUG_SPAWN_LOCATIONS = []
HISTORICAL_MOVEMENTS = []

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

def obstacle_check(object1, object2, threshold):
    list1 = MASTER_OBSTACLES[object1]
    list2 = MASTER_OBSTACLES[object2]
    #list2 = object2


    if len(list1) != len(list2):
        return 'Lists are not of the same length.'

    for point1, point2 in zip(list1, list2):

        x1, y1 = point1
        x2, y2 = point2
        check_response = int()
        if abs(x1 - x2) <= threshold and abs(y1 - y2) <= threshold:
            check_response = 1
        else:
            check_response = 0

        return check_response

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

# Initialize the board with obstacles
def initialize_obstacle_location () :
    # initialize obstacles list
    # initialize # of row/# of column
    # initiate first obstacle
    # create location for next object from list of spawn-able locations
        # If M -> threshhold is 3
        # If not M -> threshhold is 2
    #
    #
    # Initialize spawn locations
    spawn_locations()
    obstacles_list = list(MASTER_OBSTACLES)
    my_list = MASTER_BOARD

    for key, value in MASTER_OBSTACLES.items():
        spawn_object(key)

    # Iterate over the list to ensure each element is not less than 3 spaces from each other
    for i in range(1, len(MASTER_BOARD)):
        if MASTER_BOARD[i] != 'E' and MASTER_BOARD[i - 1] != 'E' and MASTER_BOARD[i] != 'W':
            if abs(i - (i - 1)) < 3:
                # Swap elements to satisfy the condition
                #if MASTER_BOARD[i] != 'W':
                MASTER_BOARD[i], MASTER_BOARD[i - 5] = MASTER_BOARD[i - 5], MASTER_BOARD[i]

    num_walls = 0
    while num_walls <  NUM_WALLS:
        my_list[random.choice(SPAWN_LOCATIONS)] = 'W'
        spawn_locations()
        num_walls += 1

    for index, value in enumerate(MASTER_BOARD):
        if value in MASTER_OBSTACLES:
            MASTER_OBSTACLES[value] = index

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






