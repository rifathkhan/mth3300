#******************************************************************************
# population.py
#******************************************************************************
# Name: 
#******************************************************************************
# Collaborators/outside sources used 
#(IMPORTANT! Write "NONE" if none were used):
#
#https://docs.python.org/2/library/math.html
#
# Reminder: you are to write your own code.
#******************************************************************************
# Overall notes (not to replace inline comments):
#
#

import math #Imports this library so that we can use mathematical functions

a = float(input("Enter initial population: "))      #Sets the variables a,b,c to the user inputs
b = float(input("Enter the first time period (in years): "))
c = float(input("Enter the first growth rate (in percentage): "))

a = a*(math.exp(b*(c/100)))     #performs the first operation

b = float(input("Enter the second time period (in years): "))       #reassigns the values of b and c to the new inputs by the user
c = float(input("Enter the second growth rate (in percentage): "))

a = a*(math.exp(b*(c/100)))    #performs the second operation

b = float(input("Enter the third time period (in years): "))        #reassigns the values of b and c again to the new inputs
c = float(input("Enter the third growth rate (in percentage): "))

a = a*(math.exp(b*(c/100))) #performs the third  operation

print("\nThe final population is {0}".format(a)) #prints out the final value of the population
