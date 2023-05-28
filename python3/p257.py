# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    @staticmethod 
    def dfs(root: Optional[TreeNode], path: List[int], paths: List[str]):
        
        if not root:
            return

        new_path = path + [root.val]

        if not root.left and not root.right:
            paths.append("->".join([str(n) for n in new_path]))

        Solution.dfs(root.left, new_path, paths)
        Solution.dfs(root.right, new_path, paths)


    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        paths = []
        Solution.dfs(root, [], paths)
        return paths

