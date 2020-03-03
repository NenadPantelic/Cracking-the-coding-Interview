#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 15:53:42 2020

@author: nenad
"""


def loop_detection(head):
    # slow node
    slow = head
    # fast 
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            break
    # loop not found
    if fast is None or fast.next is None:
        return None
    # reset slow to head
    slow = head
    # loop exists for sure if we reached this place in code
    # magical move
    while slow is not fast:
        slow = slow.next
        fast = fast.next
    return fast

class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
        
    
# Test 1
n1 = Node("A")
n2 = Node("B")
n3 = Node("C")
n4 = Node("D")
n5 = Node("E")
n6 = Node("F")
n7 = Node("G")
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
n5.next = n6
n6.next = n7
n7.next = n2
loop_start = loop_detection(n1)
print(loop_start.data if loop_start else None)


# Test 2
n1 = Node("A")
n2 = Node("B")
n3 = Node("C")
n4 = Node("D")
n5 = Node("E")
n6 = Node("F")
n7 = Node("G")
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
n5.next = n6
n6.next = n7
#n7.next = n2
loop_start = loop_detection(n1)
print(loop_start.data if loop_start else None)
        