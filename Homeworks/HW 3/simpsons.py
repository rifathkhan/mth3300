#******************************************************************************
# simpsons.py
#******************************************************************************
# Name: Rifat Khan
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

import math

a = float(input("Enter the lower bound of the definite integral : "))
b = float(input("Enter the upper bound of the definite integral : "))
n = int(input("Enter an even integer representing the intervals : "))

delta_x = (b - a)/n
sigma = 0

def calcIntegral (x) :
    output = (1/math.sqrt(2 * math.pi)) * (math.pow(math.e,(-x ** 2)/2))
    return output

for i in range(0,n+1):
    if i == 0 or i == n :
        var = 1
    elif i % 2 != 0:
        var = 4
    else:
        var = 2
    x = a + i * delta_x
    sigma += var * calcIntegral(x)
    
integralValue = (delta_x / 3) * sigma

print(integralValue)
        