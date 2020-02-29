#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 29 19:40:20 2020

@author: nenad
"""


#1.3.
'''
URLify: Write a method to replace all spaces in a string with '%20'. You may assume that the string
has sufficient space at the end to hold the additional characters, and that you are given the "true"
length of the string. (Note: If implementing in Java, please use a character array so that you can
perform this operation in place.)

'''
# O(n)

def urlify(string):
    new_str = []
    i = 0
    while i < len(string):
        if string[i] != " ":
            new_str.append(string[i])
            i += 1
        else:
            while i < len(string) and string[i] == " ":
                i += 1
            new_str.append("%20")
    return "".join(new_str)

#Test 1
str1 = "Mr John    Smith"
print(urlify(str1))
# Test 2
str2 = "M r John S m i t h "
print(urlify(str2))