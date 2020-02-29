#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 29 18:41:52 2020

@author: nenad
"""


# 1.1.
'''
Is Unique: Implement an algorithm to determine if a string has all unique characters. What if you
cannot use additional data structures?
'''

def is_unique(string):
    # roughly O(n)
    chars = set()
    for char in string:
        if char in chars:
            return False
        chars.add(char)
    return True

def is_unique2(string):
    str_sorted = sorted(string)
    for i in range(len(str_sorted)-1):
        if str_sorted[i] == str_sorted[i+1]:
            return False
    return True

def is_unique3(string):
    # only works for ASCII chars
    if len(string) > 128:
        return False
    
    bitmap = [False for i in range(128)]
    for char in string:
        position = ord(char)
        # char is already seen
        if bitmap[position] == True:
            return False
        bitmap[position] = True
    return True
    

# Test 1
str1 = "qwertyuiop"
print(is_unique(str1))
print(is_unique2(str1))
print(is_unique3(str1))


# Test 1
str1 = "qwertywuiop"
print(is_unique(str1))
print(is_unique2(str1))
print(is_unique3(str1)) 
