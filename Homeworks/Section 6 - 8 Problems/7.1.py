# -*- coding: utf-8 -*-
"""
Created on Wed May 15 14:28:03 2019

@author: khanr
"""

#Section 7 Question 1

import math as m

#******************************************************************************

class Circle:
    
    def __init__(self,r,h,k):
        self._rad = r
        self._h = h
        self._k = k
        
    def isInside(self,xC,yC):
        distance = m.sqrt(m.pow(self._h - xC,2) + m.pow(self._k - yC,2))
    
        if distance <= self._rad:
            return True
        else:
            return False 
    
    def __str__(self):
        equation = "(x - {0})^2 + (y - {1})^2 = {2}".format(self._h,self._k,self._rad**2)
        return equation

#******************************************************************************

def main():
    my_circ = Circle(3,4,2)
    myX = float(input("Enter an x-coordinate: "))
    myY = float(input("Enter an y-coordinate: "))
    within = my_circ.isInside(myX,myY)

    if within:
        print("\nInside!")
    else:
        print("\nNot inside")
        
    print(my_circ)

main()