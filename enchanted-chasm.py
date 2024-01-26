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
#user_wall_choice = 1
MASTER_OBSTACLES = {'W':[], 'M':[], 'H':[], 'T':[], 'P':[]}
MASTER_ENVIRONMENT_RELATIONSHIP = {'HM' : 3, 'HP' : 2, 'HT' : 2, 'PT' : 2, 'MT' :3 , 'MP' : 3} # Covers the relationship between Hero, Monster, Treasure, and Pit
MASTER_BOARD = []
MASTER_OBSTACLE_LOCATIONS = []
MASTER_SPAWN_LOCATIONS = []
DEBUG_SPAWN_LOCATIONS = []
HISTORICAL_MOVEMENTS = []

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

# Define the constraints when placing H, T, P, M on the board
'''def obstacle_check(object) :
    #  Update MASTER_OBSTACLES to reflect the different relationships
    lstKeys = list(MASTER_OBSTACLES.keys())

    # Constant for N spaces from obstacle being compared
    k_obs = 3
    check_value = 'T'

    # Calculate upper and lower bounds to check if an obstacle is N spaces close
    l = []
    r = MASTER_OBSTACLES[object][0]
    c = MASTER_OBSTACLES[object][1]
    r_l = MASTER_OBSTACLES[object][0] - 3
    c_l = MASTER_OBSTACLES[object][1] - 3



    r_upper_bound = 2 * k_obs + 1 + r_l
    c_upper_bound = 2 * k_obs + 1 + c_l

    #while r_l < r_upper_bound:
    if abs(r_l - MASTER_OBSTACLES[check_value][0]):
        i = c_l
        while i < c_upper_bound:
            if abs(i - MASTER_OBSTACLES[check_value][1]) <= k_obs:
                print('Choose new row')
            i += 1
    else:
        j = c_l
        while j < c_upper_bound:
            if abs(j - MASTER_OBSTACLES[check_value][1]) <= k_obs:
                print('Choose new col')
            j += 1

        #r_l += 1
'''

def obstacle_check(list1, list2, threshold=2):

    if len(list1) != len(list2):
        return "Lists are not of the same length."

    for point1, point2 in zip(list1, list2):
        x1, y1 = point1
        x2, y2 = point2

        if abs(x1 - x2) <= threshold and abs(y1 - y2) <= threshold:
            return "Need to find a new location"
        else:
            return f"Dont need to move"



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
def debug_spawn_locations () :
    rows = len(MASTER_BOARD)

    if len(DEBUG_SPAWN_LOCATIONS) > 0:
        DEBUG_SPAWN_LOCATIONS.clear()
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
        MASTER_OBSTACLES.update({obstacles_list[i] : [(ran_row, ran_col)]})

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
        MASTER_OBSTACLES.update({heros_list[i]: [(ran_row, ran_col)]})

        MASTER_BOARD[ran_row][ran_col] = heros_list[i]

        i += 1
    return MASTER_OBSTACLES


# Initialize the game
def initialze_board () :
    game_board(20, 20)
    initialize_obstacle_location(MASTER_BOARD)
    obstacle_locations(MASTER_BOARD)
    spawn_locations(MASTER_BOARD)
    spawn_hero()
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



