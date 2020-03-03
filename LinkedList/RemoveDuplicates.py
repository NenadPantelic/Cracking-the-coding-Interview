#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 10:42:52 2020

@author: nenad
"""
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
"""
Remove Dups: Write code to remove duplicates from an unsorted linked list.
FOLLOW UP
How would you solve this problem if a temporary buffer is not allowed?

"""
# O(n) - time and space
def remove_duplicates(head):
    values = set()
    node = head
    prev_node = node
    while node:
        # value already seen - skip the node, connect previous node with the next one, ommit current one
        if node.data in values:
            prev_node.next = node.next
        else:
            # add value to set
            values.add(node.data)
            # move prev node to curret node
            prev_node = node
        node = node.next
        
    return head

# O(n^2)            
def remove_duplicates(head):
    node = head
    runner_node = node.next
    while node:
        # we remove every duplicate of node value in this iteration
        runner_node = node.next
        prev_node = node
        while runner_node:
            if runner_node.data == node.data:
                prev_node.next = runner_node.next
                
            else:
                prev_node = runner_node
            runner_node = runner_node.next
        node = node.next
    return head
        
                

def print_list(head):
    node = head
    while node:
        print(node.data, end=" ")
        node = node.next
    print()

n1 = Node(2)
n2 = Node(4)
n3 = Node(1)
n4 = Node(2)
n5 = Node(3)
n6 = Node(1)
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
n5.next = n6
head = remove_duplicates(n1)
print_list(head)