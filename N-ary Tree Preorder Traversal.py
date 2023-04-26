"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    # this function will return the preorder traversal of the n-ary tree
    def preorder(self, root: 'Node') -> List[int]:
        # create a list to store the preorder traversal values
        preorder_val = []
        # this function will return the preorder traversal of the n-ary tree
        def recursive_helper(root):
            # if the root is None, return
            if root == None:
                return
            # append the value of the root to the preorder_val
            preorder_val.append(root.val)
            # iterate over the children of the root and call the recursive_helper function
            for child in root.children:
                recursive_helper(child)
        # call the recursive_helper function
        recursive_helper(root)
        # return the preorder_val
        return preorder_val
