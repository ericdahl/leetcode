# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    @staticmethod
    def traverse(root: Optional[TreeNode], level:int, sums: Dict[int, int]):
        if not root:
            return

        sums[level][0] += 1
        sums[level][1] += root.val
        Solution.traverse(root.left, level + 1, sums)
        Solution.traverse(root.right, level + 1, sums)


    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        
        sums = defaultdict(lambda: [0, 0])
        Solution.traverse(root, 0, sums)

        return [sums[i][1] / sums[i][0] for i in range(len(sums))]
