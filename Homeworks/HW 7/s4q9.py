# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

n = int(input("Enter number of rows: "))
star = "*"

for row in range(1,n+1):
    if row <= 2:
        for j in range(row):
            print(star,end="")
    else:
        print(star,end="")
        for sp in range(row-2):
            print(" ",end="")
        print(star,end="")
    print("")
    
