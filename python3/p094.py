# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    @staticmethod
    def traverse(root: Optional[TreeNode], visited:List[int]):

        if not root:
            return

        if root.left:
            Solution.traverse(root.left, visited)

        visited.append(root.val)

        if root.right:
            Solution.traverse(root.right, visited)


    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        visited = []

        self.traverse(root, visited)

        return visited


