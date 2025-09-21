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

        to_add = 0
        if root.val >= low and root.val <= high:
            to_add = root.val

        return to_add + Solution.rangeSumBST(self, root.left, low, high) + Solution.rangeSumBST(self, root.right, low, high)
