#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 09:54:43 2020

@author: nenad
"""

# prettify this code - create helper methods to reduce code size and make it modular
class ThreeStack:
    # second approach is to declare fixed size of all substacks
    def __init__(self, cap = None):
        self.cap = cap if cap else 30
        self.stack = [None] * self.cap
        self._cap1 = self.cap // 3
        self._cap2 = self.cap  // 3
        self._cap3 = self.cap - self._cap1 - self._cap2
        
        self._count1 = 0
        self._count2 = 0
        self._count3 = 0
        
    def push(self, val, stack):
        if stack not in (1,2,3):
            raise Exception("Unexisting stack") 
        # stack is full
        if stack == 1:
            if self._count1 >= self._cap1:
                raise Exception("Stack 1 is full.")
            self.stack[self._count1] = val
            self._count1 += 1
        if stack == 2:
            if self._count2 >= self._cap2:
                raise Exception("Stack 2 is full.")
            self.stack[self._cap1 + self._count2] = val
            self._count2 += 1
        
        if stack == 3:
            if self._count3 >= self._cap3:
                raise Exception("Stack 3 is full.")
            self.stack[self._cap1 + self._cap2 + self._count3] = val
            self._count3 += 1
            
    def pop(self, stack):
        if stack not in (1,2,3):
            raise Exception("Unexisting stack") 
        if stack == 1:
            if self._count1 == 0:
                raise Exception("Stack 1 is empty.")
            val = self.stack[self._count1-1]
            self.stack[self._count1-1] = None
            self._count1 -= 1
        if stack == 2:
            if self._count2 == 0:
                raise Exception("Stack 2 is femptyull.")
            val = self.stack[self._cap1 + self._count2 - 1]
            self.stack[self._cap1 + self._count2-1] = None
            self._count2 -= 1
        
        if stack == 3:
            if self._count3 == 0:
                raise Exception("Stack 3 is empty.")
            val = self.stack[self._cap1 + self._cap2 + self._count3 - 1]
            self.stack[self._cap1 + self._cap2 + self._count3 - 1] = None
            self._count3 -= 1
        return val
            
ts = ThreeStack(15)
ts.push(5, 2)
ts.push(5, 1)
ts.push(5, 2)
ts.push(5, 3)
ts.push(5, 3)
ts.push(5, 3)
ts.push(5, 3)
ts.push(5, 3)
ts.push(5, 2)
ts.push(4, 2)
ts.push(10, 2)

print(ts.stack)

print(ts.pop(1))     
print(ts.stack)
print(ts.pop(2))
print(ts.pop(2))
print(ts.pop(2))     
print(ts.stack)
   
            