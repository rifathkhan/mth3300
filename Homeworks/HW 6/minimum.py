#******************************************************************************
# minimum.py
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

c0 = float(input("Enter the x^0 coefficient: "))
c1 = float(input("Enter the x^1 coefficient: "))
c2 = float(input("Enter the x^2 coefficient: "))
c3 = float(input("Enter the x^3 coefficient: "))
x0 = float(input("Guess the x_0: "))

def calcFunction (x) :
    p_of_x = x**4 + (c3 * x**3) + (c2 * x**2) + (c1 * x) + c0
    return p_of_x

def calcDerivative (x) :
    d_of_x = (4 * x**3) + (3 * c3 * x**2) + (2 * c2 * x) + c1
    return d_of_x

def calc2ndDerivative (x):
    e_of_x = (12 * x**2) + (6 * c3 * x) + (2 * c2)
    return e_of_x

def newtonsMethod (x) :
    xnew = x - calcDerivative(x)/calc2ndDerivative(x)
    return xnew


testnum = x0

not_close_enough = True

while not_close_enough:
    testnum = newtonsMethod(testnum)

    if abs(calcDerivative(testnum)) < 10**-8:
        solution = testnum
        not_close_enough = False


print("The x value of the minimum is",solution)
print("Minumum value of  p(x) is", calcFunction(solution))
