#******************************************************************************
# triangle.py
#******************************************************************************
# Name: 
#******************************************************************************
# Collaborators/outside sources used 
#(IMPORTANT! Write "NONE" if none were used):
#
#https://www.cut-the-knot.org/pythagoras/cosine2.shtml
#https://docs.python.org/3/library/math.html
#https://stackoverflow.com/questions/35457203/python-restart-program-in-if-statement-based-on-user-input
#
# Reminder: you are to write your own code.
#******************************************************************************
# Overall notes (not to replace inline comments):
# This program allows you to calculate all three angles of a triangle given the values of the three sides in descending order
#

import math #Imports this library so we can use mathematical functions in our program

print("Use this tool to calculate the angles in a triangle!")

while True:     #This while loop is in place so that if the user enters the input correctly the program can restart.
    a = float(input("Enter largest side length: ")) #The variables a,b,and c store values based on the users input of side lengths
    b = float(input("Enter middle side length: ")) #The numbers are entered in str format. The function float() turns the str literal into a float literal
    c = float(input("Enter smallest side length: "))
    if a > b > c > 0:   #The first if statement checks if the numbers were entered in descending order
            if a + b > c and b + c > a and a + c > b:   #The second if statement checks for the validity of the triangle inequality rule
                largest_angle = (math.acos((a**2-(b**2+c**2))/(-2*b*c)))    #law of Cosine
                
                print("The largest angle is ",math.degrees(largest_angle))
                
                medium_angle = math.asin(((math.sin(largest_angle)*b)/a))   #Law of Sine
                
                print("The medium angle is ", math.degrees(medium_angle))
                
                smallest_angle = (180 - (math.degrees(largest_angle) + math.degrees(medium_angle)))
                
                print("The smallest angle is",(smallest_angle))
                break   #ends the while loop and doesnt go through with the rest of the if statements. 
            else:
                print("\nThese side lengths do not make a triangle, try again!")  #Returns the following statements if the user enters information incorrectly. Since the while loop is still true it restarts the program.
               
    else:
        print("\nSide lengths were not entered in descending order, try again!") #Returns this statement if the numbers were not entered in the correct order. Since the while loop is still true it restarts the program.
        