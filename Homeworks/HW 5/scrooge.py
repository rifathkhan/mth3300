#******************************************************************************
# scrooge.py
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

import random

coins = [0.25 , 0.1 , 0.05 , 0.01]

sum_coins = 0 ; win = 0 ; num_games = 10 ** 5; money_won = 0

for i in range(num_games):    
    for i in range(10):
        index = random.randint(0,3)
        coin_value = coins[index]
        sum_coins += coin_value
        
    if sum_coins >= 1:
        win += 1
        money_won += sum_coins
    else: 
        money_won -= 1
    sum_coins = 0
    
#print(sum_coins, money_won, win)

        
winning_percentage = ((win / num_games) * 100)
average_winnings = money_won / num_games
    
print("We won {0:.6f}% of the time".format(winning_percentage))
print("Our average winnings per game were ${0:.3f}".format(average_winnings))