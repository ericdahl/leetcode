class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i_index, i in enumerate(nums):
            for j_index in range(i_index + 1, len(nums)):
                j = nums[j_index]
                # print(i, j, i_index, j_index)
                if i + nums[j_index] == target:
                    return [i_index, j_index]