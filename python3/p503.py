class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        nums_len = len(nums)
        nge = [-1] * nums_len

        stack = []

        for i in range(2 * nums_len):
            n = nums[i % nums_len]

            while stack and nums[stack[-1]] < n:
                nge[stack.pop()] = n

            if i < len(nums):
                stack.append(i % nums_len)

        return nge
