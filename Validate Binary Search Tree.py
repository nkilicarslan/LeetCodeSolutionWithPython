# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def is_valid_recursive(root,left_or_right_child,val,path_min):
            if root == None:
                return True
            if left_or_right_child == 'left':
                if root.val < val and root.val < path_min:
                    return is_valid_recursive(root.left,'left',root.val,root.val) and is_valid_recursive(root.right, 'right', root.val,root.val)
                else:
                    return False
            else:
                if val < root.val and root.val > path_min:
                    return is_valid_recursive(root.left, 'left', root.val,path_min) and is_valid_recursive(root.right, 'right',
                                                                                                  root.val,path_min)
                else:
                    return False
        return is_valid_recursive(root.left, 'left', root.val,root.val) and is_valid_recursive(root.right, 'right', root.val,root.val)


