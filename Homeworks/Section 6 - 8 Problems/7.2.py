# -*- coding: utf-8 -*-
"""
Created on Wed May 15 14:49:28 2019

@author: khanr
"""

#Section 7 Question 2

class Line:
    
    def __init__(self,slope,yint):
        self._m = slope
        self._b = yint
        
    def yInt(self):
        return self._b
    
    def xInt(self):
        return (-self._b/self._m)
    
    def y_value(self,x):
        return (self._m * x) + self._b
        
def loop(line):
    x_vals = [4.1, 5.2, 8.3, 9.1, 6.1]
    
    for x in x_vals:
        yval = line.y_value(x)
        print(yval)
        
def main():
    pretty_line = Line(4,2)
    
    x_int = pretty_line.xInt()
    y_int = pretty_line.yInt()
    
    print("The x intercept for the pretty line is {0}, the y intercept is {1}".format(x_int,y_int))
    
    loop(pretty_line)
    
main()

