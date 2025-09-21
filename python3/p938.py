# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:

        if not root:
            return 0

        # if current value is less than low bounds, only look at right subtree
        if root.val < low:
            return Solution.rangeSumBST(self, root.right, low, high)

        if root.val > high:
            return Solution.rangeSumBST(self, root.left, low, high)

        return root.val + Solution.rangeSumBST(self, root.left, low, high) + Solution.rangeSumBST(self, root.right, low, high)
