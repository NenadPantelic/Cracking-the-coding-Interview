#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 29 20:02:54 2020

@author: nenad
"""


# 1.6. String compression
"""
String Compression: Implement a method to perform basic string compression using the counts
of repeated characters. For example, the string aabcccccaaa would become a2blc5a3 , If the
"compressed" string would not become smaller than the original string, your method should return
the original string. You can assume the string has only uppercase and lowercase letters (a - z).

"""

# O(n)
def str_compress(string):
    new_string = []
    i = 0
    while i < len(string)-1:
        el = string[i]
        count = 1
        while i < len(string)-1 and string[i] == string[i+1]:
            count += 1
            i += 1
        else:
            i += 1
        new_string.append(el)
        new_string.append(str(count))
    
    return string if len(string) <= len(new_string) else "".join(new_string)


# Test 1
string = "aabcccccaaa"
print(str_compress(string))    


# Test 2
string = "aaaaaaaaa"
print(str_compress(string))    

# Test 3
string = "abcdefg"
print(str_compress(string))    


# Test 4
string = "qwertyuiopp"
print(str_compress(string))    