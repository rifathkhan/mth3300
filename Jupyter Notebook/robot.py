#******************************************************************************
# robot.py
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
# This code should be uncommented and run
# after you write __init__
################################################################################
"""
test_game = Robogame()
print(test_game._prize, test_game._robot, "(should be two 2-element lists, different for each run)")
"""


################################################################################
# This code should be uncommented and run
# after you write .set_robot() and .set_prize()
################################################################################
"""
test_game.set_robot(2,3)
test_game.set_prize(3,4)
print(test_game._robot, test_game._prize, "(should be [2,3], [3,4])")
"""


################################################################################
# This code should be uncommented and run
# after you write .display()
################################################################################
"""
print("You should see a grid below with one R and one P: ")
test_game.display()
"""


################################################################################
# This code should be uncommented and run
# after you write .win()
################################################################################
"""
print(test_game.win(), "(should be False)")
test_game.set_robot(1,4)
test_game.set_prize(1,4)
print(test_game.win(), "(should be True)")
"""


################################################################################
# This code should be uncommented and run
# after you write .off_grid()
################################################################################
"""
print(test_game.off_grid(), "(should be False)")
test_game.set_robot(-1,2)
print(test_game.off_grid(), "(should be True)")
"""


################################################################################
# This code should be uncommented and run
# after you write .step()
################################################################################
"""
test_game.set_robot(3,3)
test_game.display()
print("Robot should move one square in a random direction each time:")
test_game.step()
test_game.display()
test_game.step()
test_game.display() 
"""
