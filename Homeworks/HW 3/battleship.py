#******************************************************************************
# battleship.py
#******************************************************************************
# Name: 
#******************************************************************************
# Collaborators/outside sources used 
#(IMPORTANT! Write "NONE" if none were used):
#
#
#
# Reminder: you are to write your own code.
#******************************************************************************
# Overall notes (not to replace inline comments):
#
#

adjacent = False

coordinate1 = int(input("Enter x coordinate of square one: "))
coordinate2 = int(input("Enter y coordinate of square one: "))
coordinate3 = int(input("Enter x coordinate of square two: "))
coordinate4 = int(input("Enter y coordinate of square two: "))

#checks if the coordinates presented are on the grid

if not 1 <= coordinate1 <= 4 or not 1 <= coordinate2 <= 4 or not 1 <= coordinate3 <= 4 or not 1 <= coordinate4 <= 4:
    print("Square(s) not on grid")
else:   #The first if statement checks if the two x coordinates can possibly be adjacent to each other
    if (coordinate1 == 1 and coordinate3 == 2) or (coordinate1 == 2 and 1 <= coordinate3 <= 3) or (coordinate1 == 3 and 2 <= coordinate3 <= 4) or (coordinate1 == 4 and coordinate3 == 3):
        adjacent = True   #The nested if checks if the y coordinates can possibly be adjacent
        if (coordinate2 == 1 and coordinate4 == 2) or (coordinate2 == 2 and 1 <= coordinate4 <= 3) or (coordinate2 == 3 and 2 <= coordinate4 <= 4) or (coordinate2 == 4 and coordinate4 == 3):
            adjacent = True
        else: 
            adjacent = False  #the variable adjacent serves as a flag and keeps check of the fact if they are adjacent or not.
    else: 
        adjacent = False

if adjacent: #prints the correct string according to the value of adjacent.
    print("Valid")        
else:
    print("Non-adjacent squares")