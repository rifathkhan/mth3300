# -*- coding: utf-8 -*-
"""
Created on Wed May 15 23:23:33 2019

@author: khanr
"""

class Section():
    def __init__(self,mxmum,names):
        self._capacity = mxmum
        self._current_num = 1
        self._participants = names
        
    def enroll(self,s):
        if self._current_num < self._capacity:
            self._participants += s
            self._current_num += 1
            return True
        else:
            return False
        
def main():
    cap = 5
    new_students = ["James","Rifat","John","Bartholowmew","Jazz","Alan"]
    
    ef3300 = Section(cap,["Evan"])
    
    for students in new_students:
        if ef3300._current_num <= cap:
            ef3300.enroll(students)   
            print("{} enrolled!".format(students))
        else:
            print("{} not enrolled".format(students))
        
main()