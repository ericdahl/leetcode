# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:

        nodes = []

        def traverse(root: Optional[TreeNode], level):
            if not root:
                return
            if len(nodes) == level:
                nodes.append([])

            nodes[level].append(root.val)
            traverse(root.left, level + 1)
            traverse(root.right, level + 1)

        traverse(root, 0)

        return nodes[::-1]
        