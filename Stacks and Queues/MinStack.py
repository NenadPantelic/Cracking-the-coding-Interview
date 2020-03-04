#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 10:23:36 2020

@author: nenad
"""


class MyStack:
    def __init__(self):
        self._stack = []
        self._minn = None

    def push(self, value):
        if len(self._stack)  == 0:
            self._minn = value
            self._stack.append(value)
            return
        if value > self._minn:
            # not candidate for minn
            self._stack.append(value)
        else:
            # new min found, correlate old min and new min, instead of new min we save difference between new min and old min
            # so we can easily get previous min
            self._stack.append(value - self._minn)
            self._minn = value
    
    def pop(self):
        if len(self._stack) == 0:
            self._minn = None
            return -1
        val = self._stack.pop(-1)
        ans = val
        if val <= self._minn:
            ans = self._minn
            self._minn = self._minn - val
        return ans
    def min(self):
        if len(self._stack) == 0:
            self._minn = None
            return -1
        return self._minn
    
    
ms = MyStack()
ms.push(79)
print(ms._stack)
print(ms.min())
print(ms._stack)

ms.push(4)
print(ms._stack)

print(ms.min())
print(ms.min())
print(ms._stack)

print(ms.pop())
print(ms._stack)

ms.push(61)
print(ms._stack)

print(ms.min())
