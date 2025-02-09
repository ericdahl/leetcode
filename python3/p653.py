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
        nums = Solution.traverse(root)

        left = 0
        right = len(nums) - 1
        while left < right:
            total = nums[left] + nums[right]
            if total == k:
                return True
            elif total < k:
                left += 1
            else:
                right -= 1

        return False