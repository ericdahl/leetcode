# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        if not root:
            return

        def preorder(node: Optional[TreeNode], l: List[TreeNode]) -> None:
            if not node:
                return
            l.append(node)
            preorder(node.left, l)
            preorder(node.right, l)

        l = []
        preorder(root, l)

        node = root
        l.pop(0)
        while l:
            node.right = l.pop(0)
            node.left = None
            node = node.right


        return root