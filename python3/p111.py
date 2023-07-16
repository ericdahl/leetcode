# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    @staticmethod
    def min_depth(root: Optional[TreeNode]) -> int:

        if not root:
            return 99999

        if root and not root.left and not root.right:
            return 1

        return 1 + min(Solution.min_depth(root.left), Solution.min_depth(root.right))

    def minDepth(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0

        return Solution.min_depth(root)