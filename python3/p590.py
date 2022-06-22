"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:

    @staticmethod
    def traverse(root: Optional[TreeNode], visited:List[int]):

        if not root:
            return

        for child in root.children:
            Solution.traverse(child, visited)

        visited.append(root.val)


    def postorder(self, root: 'Node') -> List[int]:
        visited = []

        self.traverse(root, visited)

        return visited




