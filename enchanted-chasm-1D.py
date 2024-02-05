'''
Program Name: enchanted-chasm-1D.py
GitHub Repository: https://github.com/mjanders6/Enchanted-Chasm
Author: Michael J. Anderson
Date: 04Feb2024


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
    Build the game board 1x20
        Create a range from 0 to less than 20
        Loop through each element
            If the element is at 0 or 19 set it to W
            Else set it to E
        Return the board

    Define spawnable locations to be used when placing the hero and obstacles on the board
        Loop through the board
            if an element is E
                store it in a separate list with the same location

    Initialize the pit, wall, hazards, and hero
        Ask the user how many walls are going to be placed
            If number is <= 0 or > 13
                Ask the user to renter a number between 1 and 13
        Place elements on the board
            Get the list of spawnable locations
                Randomly place the elements on the board one at a time
                    Check if 
                        Monster must not be placed within three squares of the Treasure and Pit
                        Pit must not be placed within two squares from the Treasure
                        Hero must not be placed
                            within three squares from the Monster
                            within two squares from the Pit and Treasure
                        Hero, Treasure, Pit, and Monster cannot be placed within a Wall
                Get the list of spawnable locations
                Loop until all elements are placed on the board
            Get the list of spawnable locations
                Randomly place the number of walls on the board
    Display the board on the screen

'''
import random

# Function to build a Wall
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
    #
    cols = len(MASTER_BOARD)
    j = 0
    while j < cols:
        if (MASTER_BOARD[j] == 'W') or (MASTER_BOARD[j] == 'P') or (MASTER_BOARD[j] == 'H') or (MASTER_BOARD[j] == 'T') or (MASTER_BOARD[j] == 'M') or (MASTER_BOARD[j] == ' '):
            OBSTACLE_LOCATIONS.append(j)
        j += 1

    return OBSTACLE_LOCATIONS

# Store a list of locations where a location is blank
def spawn_locations () :
    SPAWN_LOCATIONS.clear()
    cols = len(MASTER_BOARD)
    j = 0
    while j < cols:
        if (MASTER_BOARD[j] == 'E') :
            SPAWN_LOCATIONS.append(j)
        j += 1

    return SPAWN_LOCATIONS

# Debug list, clean view, to show where the obstacles are for a larger board
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

# Check if elements being placed are not within a cretain distance of other elements
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
    
    # Create a dictionary that stores the locations of the elements that are not the current object 
    while c_l <= c_upper_bound:
        if c_l > 0 and c_l < 20 and MASTER_BOARD[c_l] != object and MASTER_BOARD[c_l] != '' and MASTER_BOARD[c_l] != 'W':
            OBSTACLE_CHECK_LIST.update({MASTER_BOARD[c_l]: c_l})
        c_l += 1


    # Check the differenace between elemetns to see if they are within tolerance of placement requirements
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
    # Initialize variables
    obj_list = ['T', 'P', 'M', 'H']

    user_input = int(input(f'Enter the number of walls?\nResponse: '))
    # The number of walls must be obtained by the user (at least three(3)… the ends and at least one interior)
    while user_input <= 0 or user_input > 13:
        if user_input <= 0:
            user_input = int(input(f'The number cant be 0 or less.\nPlease enter a number between 1 and 13?\nResponse: '))
        elif (user_input > 13):
            user_input = int(input(f'That number is greater than 13.\nPlease enter a number between 1 and 13?\nResponse: '))

    # Check to see if the check function returns a 1. If it does respawn
    for i in obj_list:
        spawn_object(i)
        while obstacle_check(i) == 1:

            for index, value in enumerate(MASTER_BOARD):
                if i == value:
                    MASTER_BOARD[index] = 'E'
            spawn_object(i)

    spawn_wall('W', user_input)


# Spawn a wall
def spawn_wall(object, num_walls) :
    spawn_locations()

    wall_num = 0
    while wall_num < num_walls:
        ran_col = random.choice(SPAWN_LOCATIONS)
        # place W on the board
        MASTER_BOARD[ran_col] = object
        wall_num += 1
    # Update tables
    obstacle_locations()
    debug_spawn_locations()
    spawn_locations()

# Spawn an object H, M, W, T, P
def spawn_object (object) :
    spawn_locations() # uses spawnable locations
    rows = len(SPAWN_LOCATIONS) - 1

    ran_col = random.choice(SPAWN_LOCATIONS)
    # Check to see if location is not within a certain amount of spaces
    MASTER_OBSTACLES.update({ object : ran_col})
    MASTER_BOARD[ran_col] = object

    obstacle_locations()
    debug_spawn_locations()
    spawn_locations()

def main():
    game_board(20)
    initialize_obstacle_location()
    obstacle_locations()
    spawn_locations()
    debug_spawn_locations()
    print(MASTER_BOARD)


if __name__ == "__main__":
    MASTER_OBSTACLES = {'T': 0, 'M': 0, 'H': 0, 'P': 0}
    MASTER_BOARD = []
    OBSTACLE_LOCATIONS = []
    SPAWN_LOCATIONS = []
    DEBUG_SPAWN_LOCATIONS = []
    OBSTACLE_CHECK_LIST = {'T': 0, 'M': 0, 'H': 0, 'P': 0}

    main()
