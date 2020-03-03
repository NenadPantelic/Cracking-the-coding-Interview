#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 13:41:36 2020

@author: nenad
"""

"""
ntersection; Given two (singly) linked lists, determine if the two lists intersect. Return the inter-
secting node. Note that the intersection is defined based on reference, not value. That is, if the kth
node of the first linked list is the exact same node (by reference) as the j t h node of the second
linked list, then they are intersecting.

"""
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
        
def intersection(head_1, head_2):
    
    if head_1 is None or head_2 is None:
        return None
    len_1 = len_2 = 0
    node_1 = head_1
    node_2 = head_2
    while node_1.next:
        len_1 += 1
        node_1 = node_1.next
    while node_2.next:
        len_2 += 1
        node_2 = node_2.next
    # not mandatory - we need their difference
    len_1 += 1
    len_2 += 1
    # there is no intersection point - tails are different
    if node_1 is not node_2:
        return None
    #print(len_1, len_2)   
    offset = len_1 - len_2
    if offset > 0:
        # first list is longer
        longer = 1
    elif offset < 0:
        # second list is longer
        longer = -1
        offset = -offset
    else:
        # list have the same length
        longer = 0
    
    node_1 = head_1
    node_2 = head_2
    counter = 0
    while node_1 and node_2:
        # traverse over longer list until we reach the start of the shorter list
        if counter != offset:
            if longer == 1:
                node_1 = node_1.next
                counter += 1
            elif longer == 2:
                node_2 = node_2.next
                counter += 1
        else:
            # check until we find the intersection point
            if node_1 is node_2:
                return node_1
            else:
                node_1 = node_1.next 
                node_2 = node_2.next
    # there is no intersection point
    #return None


# Test 1
n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)
n6 = Node(6)
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
n5.next = n6
            
n7 = Node(7)
n8 = Node(8)
n7.next = n8
n8.next = n5

intersection_point = intersection(n1, n7)
print(intersection_point.data if intersection_point else None)        

    
        