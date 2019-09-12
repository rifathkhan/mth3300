#******************************************************************************
# twins.py
#******************************************************************************
# Name: 
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



################################################################################
#
# Test code for is_prime()
# Remove this when all these lines yield CORRECT
#
################################################################################
if is_prime(1):
    print("ERROR -- 1 is not prime")
else:
    print("CORRECT -- 1 is not prime")

if is_prime(2):
    print("CORRECT -- 2 is prime")
else:
    print("ERROR -- 2 is prime")
    
if is_prime(3):
    print("CORRECT -- 3 is prime")
else:
    print("ERROR -- 3 is prime")

if is_prime(5):
    print("CORRECT -- 5 is prime")
else:
    print("ERROR -- 5 is prime")

if is_prime(7):
    print("CORRECT -- 7 is prime")
else:
    print("ERROR -- 7 is prime")

if is_prime(9):
    print("ERROR -- 9 is not prime")
else:
    print("CORRECT -- 9 is not prime")

if is_prime(35):
    print("ERROR -- 35 is not prime")
else:
    print("CORRECT -- 35 is not prime")

if is_prime(143):
    print("ERROR -- 143 is not prime")
else:
    print("CORRECT -- 143 is not prime")

if is_prime(149):
    print("CORRECT -- 149 is prime")
else:
    print("ERROR -- 149 is prime")

if is_prime(21647):
    print("CORRECT -- 21647 is prime")
else:
    print("ERROR -- 21647 is prime")

if is_prime(21651):
    print("ERROR -- 21651 is not prime")
else:
    print("CORRECT -- 21651 is not prime")
