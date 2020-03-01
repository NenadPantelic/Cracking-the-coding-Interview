#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  1 10:37:23 2020

@author: nenad
"""

"""

One Away: There are three types of edits that can be performed on strings: insert a character,
remove a character, or replace a character. Given two strings, write a function to check if they are
one edit (or zero edits) away.
"""
from collections import Counter
def one_aeway(str1, str2):
    
    # lengths of strings differ for more than 1 - e.g. first string has length 4 and second one has 6
    if abs(len(str1)-len(str2)) > 1:
        return False
    
    edit_state = 0
    # possible values:
    # 0 = not edited
    # 1 = edited
    count_map_1 = Counter()
    for char in str1:
        count_map_1[char] += 1
        
    for char in str2:
        # need to be inserted
        if char not in count_map_1:
            # already edited
            if edit_state != 0:
                return False
            # edit string - insert char
            edit_state = 1
        else:
            # there is more ocurrences of char in str2 than in str1
            if count_map_1[char] <= 0:
                if edit_state !=0:
                    return False
                # insert one more piece of that char to str1
                edit_state = 1
            count_map_1[char] -= 1
        
    # reset edit state - this is for the case where we observe replace - in that case, there is one
    # char with freq = 1 and edit_state = 1 (one char from str2 is not in str1)
    # check for deletes
    edit_state = 0
    for char in count_map_1:
        # more than removal required
        if count_map_1[char] > 1:
            return False
        if count_map_1[char] == 1:
            # char is already edited  
            if edit_state == 1:
                return False
            
            # make an edit - replace
            edit_state = 1
    # otherwise            
    return True
        
            
        
# Test 1
str1 = "pale"
str2 = "pie"
print(one_aeway(str1, str2))

# Test 2
str1 = "pales"
str2 = "pale"
print(one_aeway(str1, str2))

# Test 3
str1 = "pale"
str2 = "bale"
print(one_aeway(str1, str2))

# Test 4
str1 = "pale"
str2 = "bake"
print(one_aeway(str1, str2))


# Test 5
str1 = "pale"
str2 = "bale"
print(one_aeway(str1, str2))


# Test 6
str1 = "pala"
str2 = "palo"
print(one_aeway(str1, str2))
        
    
# Test 7
str1 = "pala"
str2 = "paloa"
print(one_aeway(str1, str2))        
            

# Test 8
str1 = "pala"
str2 = "paloaa"
print(one_aeway(str1, str2))        
        
# Other idea - 
"""
if len(a) == len(b) checkForEdit
if len(a) == len(b)+1 checkForInsert
if len(a) == len(b) - 1 checkForDelete
# otherwise
return False

"""    

