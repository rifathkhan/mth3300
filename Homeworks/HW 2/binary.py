#******************************************************************************
# binary.py
#******************************************************************************
# Name: Rifat Khan
#******************************************************************************
# Collaborators/outside sources used 
#(IMPORTANT! Write "NONE" if none were used):
#
#"NONE"
#
# Reminder: you are to write your own code.
#******************************************************************************
# Overall notes (not to replace inline comments):
#
#

import random #imports this library so we can create random numbers

decimal = 0     #We will be adding on to this variable to show the decimal value of the binary

d1 = random.randrange(0,2)  #creates a random integer between 0 and 1 and sets it to variables d1-d8 which represents each digit in the binary
d2 = random.randrange(0,2)
d3 = random.randrange(0,2)  
d4 = random.randrange(0,2)
d5 = random.randrange(0,2)
d6 = random.randrange(0,2)
d7 = random.randrange(0,2)
d8 = random.randrange(0,2)

decimal = d1 + d2*2 + d3*4 + d4*8 + d5*16 + d6*32 + d7*64 + d8*128  #Takes each random value and multiples it by the value based on the place


print("Here is an example of binary")
print("The binary number",d8,d7,d6,d5,d4,d3,d2,d1, "is the same as",decimal, end = '') #prints out the binary number and the decimal equivilant.

value = int(input("Now, enter a number from 0 to 255: ")) 

binary = ''     # We wil be concatenating this string in order to write out our value of the binary
place = 128     #We start off with place equaling to 128 and this value gets halfed until it gets to 1

if value >= place:                  #These statements check whether or not the value is greater than the place value.                                                            
    binary = binary + '1'           #If it is greater "1" is concatenated to the binary variable, it it isnt it concatenates a 0.
    value = value - place           #This repeats 8 times for each binary digit and the place value is halved each time"""
    place = place/2
else:
    binary = binary + '0'
    place = place/2
    
if value >= place:
    binary = binary + '1'
    value = value - place
    place = place/2
else:
    binary = binary + '0'
    place = place/2
if value >= place:
    binary = binary + '1'
    value = value - place
    place = place/2
else:
    binary = binary + '0'
    place = place/2
    
if value >= place:
    binary = binary + '1'
    value = value - place
    place = place/2
else:
    binary = binary + '0'
    place = place/2
    
if value >= place:
    binary = binary + '1'
    value = value - place
    place = place/2
else:
    binary = binary + '0'
    place = place/2
    
if value >= place:
    binary = binary + '1'
    value = value - place
    place = place/2
else:
    binary = binary + '0'
    place = place/2
    
if value >= place:
    binary = binary + '1'
    value = value - place
    place = place/2
else:
    binary = binary + '0'
    place = place/2
    
if value >= place:
    binary = binary + '1'
    value = value - place
    place = place/2
else:
    binary = binary + '0'
    place = place/2
    
    
print("\nThis is the binary equivilant",binary)

    

