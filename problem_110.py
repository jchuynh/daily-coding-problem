# Facebook

# Given a binary tree, return all paths from the root to leaves.

#   1
#  / \
# 2   3
#    / \
#   4   5

# Return:[[1, 2], [1, 3, 4], [1, 3, 5]]

# pesudocode
# create class node
# traversal?
# store current root to leaf path 
# traverse path, storing data until you reach the end (leaf) node

class node:
    # create tree node
    def __init_(self, data):
        self.data = data
        