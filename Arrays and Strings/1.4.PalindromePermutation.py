#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  1 10:17:59 2020

@author: nenad
"""


from collections import Counter
"""
Palindrome Permutation: Given a string, write a function to check if it is a permutation of a palin-
drome. A palindrome is a word or phrase that is the same forwards and backwards. A permutation
is a rearrangement of letters. The palindrome does not need to be limited to just dictionary words.
"""

def palindrome_permutation(string):
    string = string.lower()
    counter_map = Counter()
    for char in string:
        if char == " ":
            continue
        counter_map[char] += 1
    
    # plandrome can be formed if we an even number of every char - with even length
    # or only one char with odd frequency, others have even - odd length
    odd_char_flag = False
    for char in counter_map:
        if counter_map[char] % 2 != 0:
            # there is already char with odd freq - palindrome cannot be formed
            if odd_char_flag:
                return False
            else:
                odd_char_flag = True
    return True


# Test 1
string = "Tact Coa"
print(palindrome_permutation(string))

# Test 2
string = "Tact Cooa"
print(palindrome_permutation(string))

# Test 3
string = "Tact Ccoa"
print(palindrome_permutation(string))


# Test 4
string ="aa aaa"
print(palindrome_permutation(string))

# Test 5
string ="pera"
print(palindrome_permutation(string))