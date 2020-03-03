#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 16:45:16 2020

@author: nenad
"""
"""

Partition: Write code to partition a linked list around a value x, such that all nodes less than x come
before all nodes greater than or equal to x. If x is contained within the list, the values of x only need
to be after the elements less than x (see below). The partition element x can appear anywhere in the
"right partition"; it does not need to appear between the left and right partitions.
"""
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
        
def  partition(head, x):
    if head is None:
        return None
    # ll with elements less than x
    less_ll_head = None
    # ll with element greater than or equal to x
    greater_ll_head = None
    # last added nodes for both sublists
    prev_sm_node = None
    prev_gr_node = None
    node = head
    while node:
        # add to left sublist
        if node.data < x:
            if less_ll_head is None:
                less_ll_head = node
            else:
                prev_sm_node.next = node
            prev_sm_node = node
            #prev_sm_node.next = None
        else:
            if greater_ll_head is None:
                greater_ll_head = node
            else:
                prev_gr_node.next = node
            prev_gr_node = node
            #prev_gr_node.next = None
        node = node.next
    # make tails 
    prev_sm_node.next = None
    prev_gr_node.next = None
    # concatenate lists
    prev_sm_node.next = greater_ll_head
    return less_ll_head

def print_list(head):
    node = head
    while node:
        print(node.data, end=" ")
        node = node.next
    print()
    

n1 = Node(3)
n2 = Node(5)
n3 = Node(8)
n4 = Node(5)
n5 = Node(10)
n6 = Node(2)
n7 = Node(1)
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
n5.next = n6
n6.next = n7
x = 5
head = partition(n1, 5)
print_list(head)