# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    @staticmethod
    def traverse( root: Optional[TreeNode], values: List[int]):
        if not root:
            return

        if root.left:
            Solution.traverse(root.left, values)
        if root.right:
            Solution.traverse(root.right, values)

        values.append(root.val)

    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        l = []
        Solution.traverse(root, l)
        return l