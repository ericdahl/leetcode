# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    @staticmethod
    def tilt(node: Optional[TreeNode]) -> int:
        if not node:
            return (0, 0)

        left_sum, left_tilt = Solution.tilt(node.left)
        right_sum, right_tilt = Solution.tilt(node.right)
        node_tilt = abs(left_sum - right_sum)

        return (
            node.val + left_sum + right_sum,
            left_tilt + right_tilt + node_tilt
        )

    def findTilt(self, root: Optional[TreeNode]) -> int:

        _, total_tilt = Solution.tilt(root)
        return total_tilt