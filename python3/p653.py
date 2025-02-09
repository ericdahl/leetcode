# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    @staticmethod
    def traverse(node: Optional[TreeNode]) -> List[int]:
        if not node:
            return []

        return Solution.traverse(node.left) + [node.val] + Solution.traverse(node.right)

    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        l = Solution.traverse(root)

        for i in range(len(l) - 1):
            for j in range(i + 1, len(l)):
                s = l[i] + l[j]
                if s == k:
                    return True
                if s > k:
                    continue
        return False