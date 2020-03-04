#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 12:22:32 2020

@author: nenad
"""


class SetOfStacks:
    def __init__(self, capacity):
        # capacity of one substack
        self._cap = capacity
        self._stacks = [[]]
        self._activeStack = 0
        
    def push(self, value):
        if len(self._stacks[self._activeStack]) == self._cap:
            self._stacks.append([value])
            self._activeStack += 1
        else:
            self._stacks[self._activeStack].append(value)
            
    def pop(self):
        if len(self._stacks[self._activeStack]) == 0:
            # last active stack is the first one - if it is empty, return -1
            if self._activeStack == 0:
                return -1
            # else remove it
            self._stacks.pop(self._activeStack)
            self._activeStack -= 1
            
        # return last element from active stack
        return self._stacks[self._activeStack].pop(-1)
    
    def info_print(self):
        return self._stacks
    

ss = SetOfStacks(3)
ss.push(2)
print(ss.info_print())        
ss.push(3)
ss.push(4)        
print(ss.info_print())  
ss.push(40)              
print(ss.info_print())  
print(ss.pop())
print(ss.pop())    
print(ss.info_print())          
print(ss.pop())
print(ss.pop())    
print(ss.pop())    
print(ss.info_print())            
ss.push(3)
  
print(ss.info_print())          