#******************************************************************************
# beverages.py
#******************************************************************************
# Name: Rifat Khan
#******************************************************************************
# Collaborators/outside sources used 
#(IMPORTANT! Write "NONE" if none were used):
#
#Jazz
#
# Reminder: you are to write your own code.
#******************************************************************************
# Overall notes (not to replace inline comments):
#
#

import math
import matplotlib.pyplot as plt

class Resident:
    
    def __init__(self,xcoor,ycoor,drink):
        self.xcoor = xcoor
        self.ycoor = ycoor
        self.drink = drink

    def distance(self,xcoor,ycoor):
        value = math.sqrt(math.pow(xcoor - self.xcoor,2) + math.pow(ycoor - self.ycoor,2))
        return value


x = float(input("Enter the x-coordinate of the location: "))
y = float(input("Enter the y-coordinate of the location: "))

f = open("surveydata.txt","r")

list_residents = []

pepsi = 0
coke = 0

for line in f:
    info = line.split()
    person = Resident(float(info[0]),float(info[1]),info[2])

    list_residents.append(person)

    if person.distance(x,y) <= 1 and info[2] == "Pepsi":
        pepsi += 1
    if person.distance(x,y) <= 1 and info[2] == "Coke":
        coke += 1

print("There are {0} coke drinkers and {1} pepsi drinkers near this area".format(coke,pepsi))

#Extra credit
    
for resident in list_residents:
    if resident.drink == "Pepsi":
        plt.scatter(resident.xcoor,resident.ycoor,marker = "o", color = "b")
    else:
        plt.scatter(resident.xcoor,resident.ycoor,marker = "o", color = "r")

plt.scatter(x,y,marker = "X", color = "g")

plt.show()
        



