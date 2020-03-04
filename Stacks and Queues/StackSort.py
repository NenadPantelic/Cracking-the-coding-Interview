#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 13:44:56 2020

@author: nenad
"""


def stack_sort(stack):
    # tmp stack - ascending sort  (top element is the greatest)
    stack2 = []
    while len(stack):
        # stack 2 is empty - add value
        if len(stack2) == 0:
            stack2.append(stack.pop(-1))
            continue
        # just move the element on stack2 (it follows the ascending order)
        if stack[-1] >= stack2[-1]:
            stack2.append(stack.pop(-1))
        else:
            # remove the value
            val = stack.pop(-1)
            # search for the right place for this element - move all of the element from stack2 that are greater 
            # than val
            while len(stack2) and val < stack2[-1]:
                stack.append(stack2.pop(-1))
            # right place is found - add val to stack2
            stack2.append(val)
    # move all of the elements from stack2 to stack - stack descending order sort (top element is the smallest)            
    while len(stack2):
        stack.append(stack2.pop(-1))
    return stack
            
  
# Test 1
stack = [3,1,8,2,11]
print(stack_sort(stack))



# Test 2
stack = [300,11,88,2000,1101]
print(stack_sort(stack))



# Test 3
stack = [3,4,5,6,7]
print(stack_sort(stack))