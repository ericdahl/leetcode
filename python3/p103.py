# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    @staticmethod
    def traverse(root: Optional[TreeNode], values: List[List[int]], level: int) -> None:
        if not root:
            return

        if len(values) < level + 1:
            values.append([])
            
        if level % 2 == 0:
            values[level].append(root.val)
        else:
            values[level].insert(0, root.val)

        Solution.traverse(root.left, values, level + 1)
        Solution.traverse(root.right, values, level + 1)

    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        values = []
        Solution.traverse(root, values, 0)
        return values

