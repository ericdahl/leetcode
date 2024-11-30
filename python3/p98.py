# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:


    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def recurse(node: Optional[TreeNode], min_val: int, max_val: int) -> bool:
            if not node:
                return True

            if node.val >= max_val or node.val <= min_val:
                return False

            return recurse(node.left, min_val, node.val) and recurse(node.right, node.val, max_val)

        return recurse(root, -2 **32, 2 **32)
