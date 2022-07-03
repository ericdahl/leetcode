# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    @staticmethod
    def visit(root: Optional[TreeNode], visited:list[int]):
        if not root:
            return visited

        visited.append(root.val)

        if not root.left:
            visited.append(None)
        Solution.visit(root.left, visited)

        if not root.right:
            visited.append(None)
        Solution.visit(root.right, visited)

    @staticmethod
    def hash_node(root: Optional[TreeNode]):
        visited = []
        Solution.visit(root, visited)
        return hash(tuple(visited))

        # easier but too slow? is the __str__ overridden to be artificially slow?
        # return hash(str(root))


    @staticmethod
    def search(root: Optional[TreeNode], target:int) -> bool:

        if not root:
            return False

        if Solution.hash_node(root) == target:
            return True

        if Solution.search(root.left, target):
            return True

        if Solution.search(root.right, target):
            return True

        return False

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        return Solution.search(root, Solution.hash_node(subRoot))

