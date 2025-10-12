# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    @staticmethod
    def leaves(root: Optional[TreeNode]) -> list[int]:
        if not root:
            return []

        if not root.left and not root.right:
            return [root.val]

        return Solution.leaves(root.left) + Solution.leaves(root.right)

    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        return Solution.leaves(root1) == Solution.leaves(root2)
