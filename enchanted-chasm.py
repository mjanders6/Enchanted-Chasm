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
MASTER_OBSTACLES = {'W':[], 'M':[], 'H':[], 'T':[], 'P':[]}
MASTER_ENVIRONMENT_RELATIONSHIP = {'HM' : 3, 'HP' : 2, 'HT' : 2, 'PT' : 2, 'MT' :3 , 'MP' : 3} # Covers the relationship between Hero, Monster, Treasure, and Pit
MASTER_BOARD = []
MASTER_OBSTACLE_LOCATIONS = []
MASTER_SPAWN_LOCATIONS = []
DEBUG_SPAWN_LOCATIONS = []
HISTORICAL_MOVEMENTS = []

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

def obstacle_check(object, threshold=2):
    list1 = MASTER_OBSTACLES[object]
    lstKeys = list(MASTER_OBSTACLES.keys())

    i = 0
    while (i < len(lstKeys)) :
        if (lstKeys[i] != object) and (lstKeys[i] != 'W'):

            list2 = MASTER_OBSTACLES[lstKeys[i]]
            print(i, lstKeys[i])

            if len(list1) != len(list2):
                return "Lists are not of the same length."

            for point1, point2 in zip(list1, list2):
                x1, y1 = point1
                x2, y2 = point2

                if abs(x1 - x2) <= threshold and abs(y1 - y2) <= threshold:
                    return True
                else:
                    continue

        i += 1



# Store a list of locations where a wall is
def obstacle_locations () :
    MASTER_OBSTACLE_LOCATIONS.clear()
    rows = len(MASTER_BOARD)
    i = 0
    while i < rows:
        # 
        MASTER_OBSTACLE_LOCATIONS.append([])
        cols = len(MASTER_BOARD[i])
        j = 0
        while j < cols:
            if (MASTER_BOARD[i][j] == 'W') or (MASTER_BOARD[i][j] == 'P') or (MASTER_BOARD[i][j] == 'H') or (MASTER_BOARD[i][j] == 'T') or (MASTER_BOARD[i][j] == 'M') or (MASTER_BOARD[i][j] == ' '):
                MASTER_OBSTACLE_LOCATIONS[i].append(j)
            j += 1
        i += 1
    return MASTER_OBSTACLE_LOCATIONS

# Catalog empty locations
def spawn_locations () :
    MASTER_SPAWN_LOCATIONS.clear()
    rows = len(MASTER_BOARD)
    i = 0
    while i < rows:
        #
        MASTER_SPAWN_LOCATIONS.append([])
        cols = len(MASTER_BOARD[i])
        j = 0
        while j < cols:
            if (MASTER_BOARD[i][j] == 'E') :
                MASTER_SPAWN_LOCATIONS[i].append(j)
            j += 1
        i += 1
    return MASTER_SPAWN_LOCATIONS

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
    #
    MASTER_OBSTACLES.clear()
    obstacles_list = ['W','P', 'M']
    rows = len(MASTER_BOARD) - 1
    cols = len(MASTER_BOARD[0]) - 1

    ran_row = random.sample(range(1, rows), 1)[0]
    ran_col = random.sample(range(1, cols), 1)[0]

    MASTER_OBSTACLES.update({'T' : [(ran_row, ran_col)]})
    MASTER_BOARD[ran_row][ran_col] = 'T'

    i = 0 
    while i < len(obstacles_list) :
        ran_row = random.sample(range(1, rows), 1)[0]
        ran_col = random.sample(range(1, cols), 1)[0]
        # Enforce the rules for obstacle locations

        #MASTER_OBSTACLES.update({obstacles_list[i] : [(ran_row, ran_col)]})

        #MASTER_BOARD[ran_row][ran_col] = obstacles_list[i]
        
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
        MASTER_OBSTACLES.update({heros_list[i]: [(ran_row, ran_col)]})

        MASTER_BOARD[ran_row][ran_col] = heros_list[i]

        i += 1
    return MASTER_OBSTACLES

# Spawn an object H, M, W, T, P
def spawn_object (object) :

    rows = len(MASTER_SPAWN_LOCATIONS) - 1

    current_obj_row = MASTER_OBSTACLES[object][0][0]
    current_obj_col = MASTER_OBSTACLES[object][0][1]
    MASTER_BOARD[current_obj_row][current_obj_col] = 'E'


    ran_row = random.sample(range(1, rows), 1)[0]
    ran_col = random.choice(MASTER_SPAWN_LOCATIONS[ran_row])

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



