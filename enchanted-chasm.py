'''
Program Name: P2_Anderson.py
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
    Build the board
    Build  the interrior walls
    Load the walls into the board
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
- Generate walls
- Place monster, hero, pit, treasure on the board
- Move the hero


'''
import random
#user_wall_choice = int(input('Enter the number of walls needed: '))
user_wall_choice = 3

#my_wall = ['E'] * 20
#my_wall[0] = 'W'
#my_wall[19] ='W'

def wall (row, col) :
    my_wall = []

    i = 0
    while i < row:
        # Initialize the inner list for each row
        my_wall.append([])

        j = 0
        while j < col:
            # 
            if (j == 0) or (j == 19) or (i == 0) or (i == 19):
                my_wall[i].append('w')
            else:
                my_wall[i].append('E')
            j += 1

        i += 1
    return my_wall

my_wall = wall(20, 20)

# Display the matrix
for row in my_wall:
    print(row)





    





