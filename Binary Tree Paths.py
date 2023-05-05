# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if root.left == None and root.right == None:
            return [str(root.val)]
        result_path = []

        def find_path(root,solution_path):
            if root == None:
                return
            if root.left == None and root.right == None:
                result_path.append(solution_path + "->" +str(root.val))
            else:
                find_path(root.left, solution_path + "->" +str(root.val))
                find_path(root.right, solution_path + "->" + str(root.val))

        find_path(root.left, str(root.val))
        find_path(root.right, str(root.val))
        return result_path