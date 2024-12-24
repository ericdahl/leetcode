# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    @staticmethod
    def height(node: Optional[TreeNode]) -> int:
        height = 0
        while node:
            height += 1
            node = node.left
        return height

    def countNodes(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0

        left_height = Solution.height(root.left)
        right_height = Solution.height(root.right)

        print(f"left_height={left_height} / right_height={right_height}")

        # if height of left subtree is the height of right subtree then
        # left must be fully filled in (perfect) so left subtree has 2**left_height
        # nodes, then add in the right side
        if left_height == right_height:
            return 2**left_height + self.countNodes(root.right)
        else:
            return 2**right_height + self.countNodes(root.left)
