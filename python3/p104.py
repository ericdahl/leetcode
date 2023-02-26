# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def maxDepth(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0

        if not root.right and not root.left:
            return 1

        l = Solution.maxDepth(self, root.left) if root.left else 0
        r = Solution.maxDepth(self, root.right) if root.right else 0

        return 1 + max(l, r)

