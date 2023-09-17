# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    @staticmethod
    def traverse(root: Optional[TreeNode], values: List[List[int]], level: int):
        if not root:
            return

        if len(values) < level + 1:
            values.append([])

        values[level].append(root.val)

        Solution.traverse(root.left, values, level + 1)
        Solution.traverse(root.right, values, level + 1)

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        values = []
        Solution.traverse(root, values, 0)

        return values
