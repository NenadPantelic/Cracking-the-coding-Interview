#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 14:57:24 2020

@author: nenad
"""

class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
        
def forward_sum(head_1, head_2):
    if head_1 is None: return head_2
    if head_2 is None: return  head_1
    node_1 = head_1
    node_2 = head_2
    len_1 = len_2 = 0
    # determine length of the first ll
    while node_1:
        len_1 += 1
        node_1 = node_1.next
        
    # determine length of the second ll
    while node_2:
        len_2 += 1
        node_2 = node_2.next
    
    sum_list = [0] * max(len_1, len_2)

    # determine difference in length and longer list        
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
        
    # set pointers again to head elements
    node_1 = head_1
    node_2 = head_2
    new_head = None
    counter = 0
    while node_1 and node_2:
        # traverse over longer list until we reach the start of the shorter list
        if counter < offset:
            if longer == 1:
                sum_list[counter] = node_1.data
                node_1 = node_1.next
                counter += 1
                
            elif longer == 2:
                sum_list[counter] = node_2.data
                node_2 = node_2.next
                counter += 1
        else:
            sum_list[counter] = node_1.data + node_2.data
            counter += 1
            node_1 = node_1.next 
            node_2 = node_2.next 
        
    # update values by including carry value in result
    carry = 0
    for i in range(len(sum_list)-1,-1,-1):
        total = sum_list[i] + carry
        sum_list[i] = (total) % 10
        carry = total // 10
    if carry != 0:
        sum_list.insert(0, carry)
    # create nodes with appropriate values from sum_list
    new_head = prev_node = None
    for i in range(len(sum_list)):
        node = Node(sum_list[i])
        if not new_head:
            new_head = node
            #prev_node = node
        else:
            prev_node.next = node
        prev_node = node
        
        
    return new_head

def print_list(head):
    node = head
    while node:
        print(node.data, end=" ")
        node = node.next
    print()

# Test 1
# n1 = Node(1)
# n2 = Node(8)
# n3 = Node(4)
# n4 = Node(5)
# n1.next = n2
# n2.next = n3
# n3.next = n4

# n5 = Node(6)
# n6 = Node(8)
# n7 = Node(5)
# n8 = Node(2)
# n5.next = n6
# n6.next = n7
# n7.next = n8
    
# Test 2   
# n1 = Node(9)
# n2 = Node(9)
# n3 = Node(9)
# n4 = Node(9)
# n1.next = n2
# n2.next = n3
# n3.next = n4

# n5 = Node(2)
# n6 = Node(2)
# n7 = Node(2)
# n8 = Node(2)
# n5.next = n6
# n6.next = n7
# n7.next = n8
    
    
n1 = Node(9)
n2 = Node(8)
n3 = Node(7)
n4 = Node(6)
n1.next = n2
n2.next = n3
n3.next = n4

n5 = Node(8)
n6 = Node(5)
n5.next = n6

head = forward_sum(n1, n5)
print_list(head)
    
        