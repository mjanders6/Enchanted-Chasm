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
    Generate Random numbers for the following
        4 random inegers + numbers of walls
            Min of 3 walls
            Monster
            Pit
            Hero
            Treasure
        Check 
    Replace elements in the wall list with the elements from the random numbher
        correlating to the monster, hero, pit, treasure
    
List of Functions:
- Generate board
* Generate interior walls
- Build a list where there is a wall
* Place monster, pit, treasure on the board
* Generate random spawn locations
* Move the hero


'''
import random

#user_wall_choice = int(input('Enter the number of walls needed: '))
user_wall_choice = 1

# random integers used to set locations
ran_list = random.sample(range(1, 19), 4 + user_wall_choice)

# Build NxN Wall 
def wall (row, col) :
    my_wall = []

    i = 0
    while i < row:
        # Initialize the inner list for each row
        my_wall.append([])

        j = 0
        while j < col:
            # 
            if (j == 0) or (j == 19) : # or (i == 0) or (i == 19):
                my_wall[i].append('W')
            else:
                my_wall[i].append('E')
            j += 1

        i += 1
    return my_wall

# Store a list of locations where a wall is
def wall_locations (wall) :
    my_list = []
    rows = len(wall)
    i = 0
    while i < rows:
        # 
        my_list.append([])
        cols = len(wall[i])
        j = 0
        while j < cols:
            if(wall[i][j] == 'W') :
                my_list[i].append(j)
            j += 1
        i += 1
    return my_list

def set_obstacles (wall) :
    obstacles_list = ['W','P','T','H', 'M']
    rows = len(wall)
    i = 0
    while i < rows:
        cols = len(obstacles_list)
        ran_samp_list = []
        
        j = 0
        while j < cols:
            ran_sample = random.sample(range(1, 19), 1)[0]
            
            if (ran_sample not in ran_samp_list) :
                ran_samp_list.append(ran_sample)
                wall[i][ran_sample] = obstacles_list[j]
            j += 1            
        i += 1

    return wall

###############

# Function to find the location where the pit, monster,and treasure are

# Generate random locations

# Sets an NxN wall
my_wall = wall(1, 20)
set_obstacles(my_wall)

# Creats a list of locations where there is a wall per row
w_list = wall_locations(my_wall)


# Display the matrix
for row in my_wall:
    print(row)





    





