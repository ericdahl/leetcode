# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:

        nodes = []

        def traverse(root: Optional[TreeNode], nodes, level):
            if not root:
                return
            if len(nodes) < level + 1:
                nodes.append([])

            nodes[level].append(root.val)
            traverse(root.left, nodes, level + 1)
            traverse(root.right, nodes, level + 1)

        traverse(root, nodes, 0)

        return nodes[::-1]
