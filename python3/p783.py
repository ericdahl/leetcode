# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    @staticmethod
    def traverse(root: Optional[TreeNode]) -> List[int]:

        if not root:
            return []

        return Solution.traverse(root.left) + [root.val] + Solution.traverse(root.right)

    def minDiffInBST(self, root: Optional[TreeNode]) -> int:

        l = Solution.traverse(root)

        min_diff = 10**6
        for i in range(len(l) - 1):
            min_diff = min(min_diff, l[i + 1] - l[i])

        return min_diff