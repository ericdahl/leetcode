# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def iterate(root: Optional[TreeNode], l: List[int]):
            if not root:
                return

            iterate(root.left, l)
            l.append(root.val)
            iterate(root.right, l)

        l = []
        iterate(root, l)
        return l[k - 1]