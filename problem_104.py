# Asked by Google

# Determine whether a doubly linked list is a palindrome. 
# What if it’s singly linked?

# For example, 1 -> 4 -> 3 -> 4 -> 1 returns True while 1 -> 4 returns False.

# Pseudocode - doubly linked list:
# Brute force:
# check in order, then compare reverse order to see if they match. 

# 

class Node(object):
    """Class in a linked list."""

    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def 