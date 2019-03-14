"""
Python skill test from:
https://www.testdome.com/questions/python/binary-search-tree/24973?visibility=1&skillId=9

Author:
Josip Kremenić

Score:
100% (3 pass / 0 fail)

Question:
Binary search tree (BST) is a binary tree where the value of each node is larger or 
equal to the values in all the nodes in that node's left subtree and is smaller than 
the values in all the nodes in that node's right subtree.

Write a function that, efficiently with respect to time used, checks if a given binary 
search tree contains a given value.


For example, for the following tree:

- n1 (Value: 1, Left: null, Right: null)
- n2 (Value: 2, Left: n1, Right: n3)
- n3 (Value: 3, Left: null, Right: null)
Call to contains(n2, 3) should return True since a tree with root at n2 contains number 3.
"""

######## Start Original script ########

# import collections

# Node = collections.namedtuple('Node', ['left', 'right', 'value'])

# def contains(root, value):
#     pass
        
# n1 = Node(value=1, left=None, right=None)
# n3 = Node(value=3, left=None, right=None)
# n2 = Node(value=2, left=n1, right=n3)
        
# print(contains(n2, 3))

######## End Original script ########

import collections

Node = collections.namedtuple('Node', ['left', 'right', 'value'])

def contains(root, value):
    if root == None:
        # If root is None, return False - value is not in the tree
        return False

    if value == root.value:
        # When value of the node found, return True
        return True

    if value < root.value:
        # Value of the node great the value => go left (lower number)
        return contains(root.left, value)

    if value > root.value:
        # Value of the node lower the value => go right (greater number)
        return contains(root.right, value)

    return False

n1 = Node(value=1, left=None, right=None)
n3 = Node(value=3, left=None, right=None)
n2 = Node(value=2, left=n1, right=n3)
        
print(contains(n2, 3))