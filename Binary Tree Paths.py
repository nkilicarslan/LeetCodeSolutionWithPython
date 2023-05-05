# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # this function will return all the root-to-leaf paths in the binary tree
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        # if the left and right child of the root is None, return the root value
        if root.left == None and root.right == None:
            return [str(root.val)]
        # create a list to store the result
        result_path = []
        # this function will find the path from the root to the leaf
        def find_path(root,solution_path):
            # if the root is None, return
            if root == None:
                return
            # if the left and right child of the root is None, append the solution_path to the result_path
            if root.left == None and root.right == None:
                result_path.append(solution_path + "->" +str(root.val))
            # otherwise call the function recursively for the left and right child of the root
            else:
                find_path(root.left, solution_path + "->" +str(root.val))
                find_path(root.right, solution_path + "->" + str(root.val))
        # call the function for the left and right child of the root
        find_path(root.left, str(root.val))
        find_path(root.right, str(root.val))
        # return the result_path
        return result_path
