#******************************************************************************
# quadratic.py
#******************************************************************************
# Name: Rifat Khan
#******************************************************************************
# Collaborators/outside sources used 
#(IMPORTANT! Write "NONE" if none were used):
#
#https://www.programiz.com/python-programming/methods/built-in/complex
#
# Reminder: you are to write your own code.
#******************************************************************************
# Overall notes (not to replace inline comments):
#

import math

first_coef = float(input("Enter x^2 coefficient: "))
second_coef = float(input("Enter x^2 coefficient: "))
third_coef = float(input("Enter x^2 coefficient: "))

discriminant = (second_coef**2) - (4*first_coef*third_coef) #calculates the discriminant based on the values entered

if discriminant > 0:
    dv = "TWO SOLUTIONS: "    #Checks the value of the discriminant and prints out the correct number of roots
elif discriminant == 0:
    dv = "ONE SOLUTION: "     
else:
    dv = "COMPLEX SOLUTIONS: "

if discriminant > 0:   #if the discriminant is greater than 0, it calculates the two roots using the quadratic formula and prints them out to the 4th decimal place
    root1 = (-second_coef + math.sqrt(discriminant))/(2*first_coef)
    root2 = (-second_coef - math.sqrt(discriminant))/(2*first_coef)
    print("{0} x = {1:.4f} and {2:.4f}".format(dv,root1,root2))
elif discriminant == 0: #if the discriminant is 0, then calculates out the root using the formula for vertex of a quadratic
    root1 = (-second_coef / (2*first_coef))
    print("{0} x = {1:.4f}".format(dv,root1))
else:    #otherwise calculates the complex roots and replacs j with i
    root1 = complex((-second_coef/(2*first_coef)),math.sqrt(-discriminant)/(2*first_coef))
    root2 = complex((-second_coef/(2*first_coef)),-math.sqrt(-discriminant)/(2*first_coef))
    print("{0} x = {1:.4f} and {2:.4f}".format(dv,root1,root2))
    root1 = str(root1); root1 = root1[1:-2] + "i" #turns the results to a string and performs slicing.
    root2 = str(root2); root2 = root2[1:-2] + "i"
    print("{0} x = {1} and {2}".format(dv,root1,root2))
   
    
