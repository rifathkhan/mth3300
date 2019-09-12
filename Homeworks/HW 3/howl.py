#******************************************************************************
# howl.py
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

lat = float(input("Enter latitude of restaurant: "))
long = float(input("Enter longitude of restaurant: "))
score1 = int(input("Enter first review score: "))
score2 = int(input("Enter second review score: "))
score3 = int(input("Enter third review score: "))

lat_howl =  40.740230
long_howl = -73.983766

def calc_distance (lat_rest,long_rest):   #Function that calculates the distance from the headquarters the the restaurant
    output = math.sqrt(math.pow(111.048 * (lat_rest - lat_howl),2) + math.pow(84.515 * (long_rest - long_howl),2))
    return output

distance = calc_distance(lat,long)  #This variable uses the function and keeps track of the distance

print(distance)

recommendation = "Try!"
avg_rating = (score1 + score2 + score3)/3   #Calculates the average score

print(avg_rating)

if score1 == 1 or score2 == 1 or score3 == 1 or distance > 4 or avg_rating < 2.5:   #If the restaurants scores of distance do not meet our requirements or set the recommendation to "dont try" otherwise set it to "try"
  recommendation = "Dont Try!"
elif 2 < distance < 4:
    if avg_rating <= 3.5:
        recommendation = "Dont Try!"
else:
    recommendation = "Try!"   

print(recommendation)

    
            
        


    
    
