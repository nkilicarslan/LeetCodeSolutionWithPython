# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # this function is to calculate the sum of all root-to-leaf numbers
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        # create a variable to store the sum of all root-to-leaf numbers
        sum = [0]
        # create a variable to store the current number string
        current_num = ''
        # create a helper function to recursively calculate the sum of all root-to-leaf numbers
        def helper_recursive(root, sum, current_num):
            # if the root is not None and the root.left and root.right are None
            if root and root.right == None and root.left == None:
                # update the path sum
                current_num = current_num + str(root.val)
                # add the current number to the sum
                sum[0] += int(current_num)
                # return in the base case
                return
            # if the root is not None
            elif root:
                # update the current number string
                current_num = current_num + str(root.val)
                # recursively calculate the sum of all root-to-leaf numbers with left child
                helper_recursive(root.left, sum, current_num)
                # recursively calculate the sum of all root-to-leaf numbers with right child
                helper_recursive(root.right, sum, current_num)
        # call the helper function
        helper_recursive(root, sum, current_num)
        # return the sum of all root-to-leaf numbers
        return sum[0]
