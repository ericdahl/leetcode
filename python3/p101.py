# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    @staticmethod
    def is_mirror(left: Optional[TreeNode], right: Optional[TreeNode]):
        if not left and not right:
            return True
        
        if (left and not right) or (right and not left):
            return False

        if left.val != right.val:
            return False

        return Solution.is_mirror(left.right, right.left) and Solution.is_mirror(left.left, right.right)

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        return Solution.is_mirror(root.left, root.right)

