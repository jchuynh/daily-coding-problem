# Microsoft

# Print the nodes in a binary tree level-wise. For example, the following should
# print 1, 2, 3, 4, 5.

#   1
#  / \
# 2   3
#  / \
# 4   5

# Tree Traversal

# Pseudocode:
# create class Node function

class Node:
    def__init__(self, data):
    self.left = None
    self.right = None
    self.data = data

def in_order(root):

    if root:
        in_order(root.left)

        print(root.val)

        in_order(root.right)



if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. EXCELLENT!\n")