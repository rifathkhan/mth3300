# -*- coding: utf-8 -*-
"""
Created on Wed May 15 15:57:13 2019

@author: khanr
"""

#Section 7 Number 4:

class Truck:
    def __init__(self, item, weight):
        self._items = item
        self._weights = weight
        self._cur_items = 0
        self._cur_weights = 0
        
    def addon(self,w):
        if self._cur_weights + w <= self._weights and self._cur_items + 1 <= self._items:
            self._cur_weights += w
            self._cur_items += 1
            print("TRUE")
            return True
        else:
            print("False")
            return False
        
    def lt(self):
        return self._cur_weight < self._weights

 #############                     
def main():
    biggie = Truck(80,15000)
    biggie.addon(13000)
    biggie.lt

main()
