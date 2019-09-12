#******************************************************************************
# robot.py
#******************************************************************************
# Name: Rifat Khan
#******************************************************************************
# Collaborators/outside sources used 
#(IMPORTANT! Write "NONE" if none were used):
#
#Jazz
# Reminder: you are to write your own code.
#******************************************************************************
# Overall notes (not to replace inline comments):
#
#

import random

class Robogame:

    def __init__(self):
        self._robot = [random.randint(0,5),random.randint(0,5)]
        self._prize = [random.randint(0,5),random.randint(0,5)]

    def set_robot(self,i,j):
        self._robot = [i,j]
    
    def set_prize(self,i,j):
        self._prize = [i,j]
        
    def display(self):
        grid = [
            [[0,0],[0,1],[0,2],[0,3],[0,4],[0,5]],
            [[1,0],[1,1],[1,2],[1,3],[1,4],[1,5]],
            [[2,0],[2,1],[2,2],[2,3],[2,4],[2,5]],
            [[3,0],[3,1],[3,2],[3,3],[3,4],[3,5]],
            [[4,0],[4,1],[4,2],[4,3],[4,4],[4,5]],
            [[5,0],[5,1],[5,2],[5,3],[5,4],[5,5]]
            ]
        
        for row in range(len(grid)):
            for position in range(len(grid[row])):
                if grid[row][position] == self._robot:
                    print("R",end = "")
                elif grid[row][position] == self._prize:
                    print("P",end = "")
                elif grid[row][position] == self._prize and grid[row][position] == self._robot:
                    print("C",end = "")
                else:
                    print(".",end = "")
            print("")
        print("")  
    
    def win(self):
        if self._robot == self._prize:
            return True
        else:
            return False
    
    def off_grid(self):
        if self._robot[0] > 5 or self._robot[0] < 0 or self._robot[1] > 5 or self._robot[1] < 0:
            return True
        else:
            return False
        
    def step(self):
        self._robot[random.choice([0,1])] += random.choice([-1,1])


    
simulations = 100000
wins = 0
losses = 0

for i in range(simulations):
    game = Robogame()

    while not game.off_grid():
        game.step()
        
        if game.win():
            wins += 1
            break
        else:
            losses += 1
            
print("Winning percentage = ", wins/simulations * 100)


            
            
            
            
            
            
            
            
            