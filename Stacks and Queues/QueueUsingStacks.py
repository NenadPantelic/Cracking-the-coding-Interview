#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 12:11:12 2020

@author: nenad
"""

# allowed ops: append() and pop(-1)
class MyQueue:
    def _init__(self):
        self._stack1 = []
        self._stack2 = []
        
    def push(self, val):
        self._stack1.append(val)
        
        
    def pop(self):
        # copy values from stack1 to stack2
        if len(self._stack2) == 0:
            while len(self._stack1):
                self._stack2.append(self._stack1.pop(-1))
        # if stack2 (stack for dequeueing) is not empty
        if len(self._stack2):
            return self._stack2.pop(-1)
        return -1