class Solution:

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        results = set()

        nums.sort()
        for i in range(len(nums)):

            left = i + 1
            right = len(nums) - 1

            while left < right:

                sum3 = nums[i] + nums[left] + nums[right]

                if sum3 == 0:
                    results.add((nums[i], nums[left], nums[right]))

                    left += 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
                elif sum3 > 0:
                    right -= 1
                else:
                    left += 1
        return results
