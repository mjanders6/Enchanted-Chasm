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
- Build a list where there is an obstacles and walls
* Place monster, pit, treasure on the board
* Generate random spawn locations
* Move the hero


'''
import random

#user_wall_choice = int(input('Enter the number of walls needed: '))
#user_wall_choice = 1
#MASTER_OBSTACLES = {'W':[(3, 4)], 'M':[(3, 6)], 'H':[(5, 12)], 'T':[(3, 12)], 'P':[(1, 15)]}
MASTER_OBSTACLES = {'T':[], 'M':[], 'H':[], 'P':[]}
MASTER_BOARD = []
OBSTACLE_LOCATIONS = []
SPAWN_LOCATIONS = []
DEBUG_SPAWN_LOCATIONS = []
HISTORICAL_MOVEMENTS = []

# Used to compare a list of tuples
MASTER_OBSTACLE_LOCATIONS = []
MASTER_SPAWN_LOCATIONS = []

# Build NxN Wall 
def game_board (row, col) :
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
                MASTER_OBSTACLE_LOCATIONS.append([(i, j)])
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
                MASTER_SPAWN_LOCATIONS.append([(i, j)])
            j += 1
        i += 1
    return SPAWN_LOCATIONS

# Debug, clean view, to show where the obstacles are
def debug_spawn_locations () :
    DEBUG_SPAWN_LOCATIONS.clear()
    rows = len(MASTER_BOARD)

    if len(DEBUG_SPAWN_LOCATIONS) > 0:

        i = 0
        while i < rows:
            #
            DEBUG_SPAWN_LOCATIONS.append([])
            cols = len(MASTER_BOARD[i])
            j = 0
            while j < cols:
                if (MASTER_BOARD[i][j] == 'E') :
                    DEBUG_SPAWN_LOCATIONS[i].append('')
                else :
                    DEBUG_SPAWN_LOCATIONS[i].append(MASTER_BOARD[i][j])
                j += 1
            i += 1
    else:
        i = 0
        while i < rows:
            #
            DEBUG_SPAWN_LOCATIONS.append([])
            cols = len(MASTER_BOARD[i])
            j = 0
            while j < cols:
                if (MASTER_BOARD[i][j] == 'E') :
                    DEBUG_SPAWN_LOCATIONS[i].append('')
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
    #
    #
    # Initialize spawn locations
    spawn_locations()
    obstacles_list = list(MASTER_OBSTACLES)

    for key, value in MASTER_OBSTACLES.items():
        spawn_object(key)

    rows = len(MASTER_BOARD) - 1
    cols = len(MASTER_BOARD[0]) - 1

    # Iterate over the list to ensure each element is not less than 3 spaces from each other



def spawn_hero () :
    heros_list = ['H']
    rows = len(SPAWN_LOCATIONS) - 1
    cols = len(SPAWN_LOCATIONS[0]) - 1

    # MASTER_OBSTACLES.update({'H' : [ran_row, ran_col]})

    i = 0
    while i < len(heros_list):
        ran_row = random.sample(range(1, rows), 1)[0]

        ran_col = random.choice(SPAWN_LOCATIONS[ran_row])
        MASTER_OBSTACLES.update({heros_list[i]: [(ran_row, ran_col)]})

        MASTER_BOARD[ran_row][ran_col] = heros_list[i]

        i += 1
    return MASTER_OBSTACLES

# Spawn an object H, M, W, T, P
def spawn_object (object) :
    spawn_locations()
    rows = len(SPAWN_LOCATIONS) - 1

    if MASTER_OBSTACLES[object] != []:
        current_obj_row = MASTER_OBSTACLES[object][0][0]
        current_obj_col = MASTER_OBSTACLES[object][0][1]
        MASTER_BOARD[current_obj_row][current_obj_col] = 'E'

    ran_row = random.sample(range(1, rows), 1)[0]
    ran_col = random.choice(SPAWN_LOCATIONS[ran_row])
    # Check to see if location is not within a certain amount of spaces
    MASTER_OBSTACLES.update({ object : [(ran_row, ran_col)]})
    MASTER_BOARD[ran_row][ran_col] = object

    obstacle_locations()
    debug_spawn_locations()
    spawn_locations()

# Initialize the game
def initialze_board () :
    game_board(3, 20)
    initialize_obstacle_location()
    obstacle_locations()
    spawn_locations()
    debug_spawn_locations()
    #obstacle_check('M')  # just debugging


initialze_board()

'''
where list1 = [(x, y)]
def colission(list1, list2)
    for x,y in list1:
        for a,b in list2:
            if x == a and y == b
                print(found wall)
    
'''

# Creats a list of locations where there is a wall per row









# Explore the Chasm
'''
USER_INPUT = input(f'Are you ready to exploire?\nResponse:\n1. Y\n2. N')


while USER_INPUT != 'N':
    if (USER_INPUT == 'Y') :
        initialze_board()
        USER_INPUT = input(f'Want to move or cheat?\nResponse:\n1. Cheat\n2. Move\n3. End')
        if (USER_INPUT == 1):
            cheat = debug_spawn_locations()
            for i in cheat:
                print(i)
    break


'''



