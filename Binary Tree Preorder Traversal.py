# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # create a list to store the result
        res = []
        # create a function to traverse the tree recursively
        def helper_recursive(result_list, root):
            # if the root is None, reached the base case, then return
            if root is None:
                return
            # append the root value to the result list
            result_list.append(root.val)
            # call the helper_recursive function with the left child
            helper_recursive(result_list, root.left)
            # call the helper_recursive function with the right child
            helper_recursive(result_list, root.right)
        # call the helper_recursive function with the root
        helper_recursive(res, root)
        # return the result list
        return res