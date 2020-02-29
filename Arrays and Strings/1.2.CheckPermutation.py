#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 29 19:08:26 2020

@author: nenad
"""


# 1.2.
'''
Check Permutation: Given two strings, write a method to decide if one is a permutation of the
other.
'''

# O(nlogn)
def check_permutation(str1, str2):
    if len(str1) != len(str2):
        return False
    # sort both strings - check if they are the same
    s1 = sorted(str1)
    s2 = sorted(str2)
    return s1 == s2

        
# Test 1
s1 = "qazse"
s2 = "sqzae"
print(check_permutation(s1, s2))    

# Test 2
s1 = "qazswe"
s2 = "sqzae"
print(check_permutation(s1, s2))    

# Test 3
s1 = "qazzse"
s2 = "sqzae"
print(check_permutation(s1, s2))   


# Test 4
s1 = "qazzse"
s2 = "sqzwae"
print(check_permutation(s1, s2))   



# Test 5
s1 = "qazzse"
s2 = "sqzase"
print(check_permutation(s1, s2))  

# Test 6
s1 = "qarzse"
s2 = "sqzase"
print(check_permutation(s1, s2))   

from collections import defaultdict
# on average O(n)
def check_permutation2(str1, str2):
    if len(str1) != len(str2):
        return False
    chars_1 = defaultdict(int)
    chars_2 = defaultdict(int)
    for char in str1:
        chars_1[char] += 1
    for char in str2:
        if char not in chars_1:
            # some char from first string is not present in second string
            return False
        chars_1[char] -= 1
        if chars_1[char] < 0:
            # if there is more pieces of some char in str2 than in str1
            return False
    for char in chars_1:
        if chars_1[char] != 0:
            # if there is more pieces of some char in str1 than in str2
            return False
    return True
    
        
# Test 1
s1 = "qazse"
s2 = "sqzae"
print(check_permutation2(s1, s2))    

# Test 2
s1 = "qazswe"
s2 = "sqzae"
print(check_permutation2(s1, s2))    

# Test 3
s1 = "qazzse"
s2 = "sqzae"
print(check_permutation2(s1, s2))   


# Test 4
s1 = "qazzse"
s2 = "sqzwae"
print(check_permutation2(s1, s2))   



# Test 5
s1 = "qazzse"
s2 = "sqzase"
print(check_permutation2(s1, s2))   

# Test 6
s1 = "qarzse"
s2 = "sqzase"
print(check_permutation2(s1, s2))   