# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # if the root is None return True
        if not root:
            return True
        # create a function to check if the tree is symmetric
        def helper_recursive(root1, root2):
            # if the root1 and the root2 are None return True
            if not root1 and not root2:
                return True
            # if one of the roots is None return False
            elif not root1 or not root2:
                return False
            # if the value of the root1 is equal to the value of the root2
            elif root1.val == root2.val:
                # recursively call the function with the left of the root1 and the right of the root2 and the right of the root1 and the left of the root2
                return helper_recursive(root1.left,root2.right) and helper_recursive(root1.right,root2.left)
            # else return False
            else:
                return False
        # call the helper_recursive function with the left of the root and the right of the root
        return helper_recursive(root.left,root.right)
