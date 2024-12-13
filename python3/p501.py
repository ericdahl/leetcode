# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:

        def traverse(node: Optional[TreeNode], c: Counter):
            if not node:
                return
            c[node.val] += 1
            traverse(node.left, c)
            traverse(node.right, c)

        c = Counter()
        traverse(root, c)

        frequency = 0
        result = []
        for (val, count) in c.most_common():
            if count < frequency:
                break
            result.append(val)
            frequency = count

        return result