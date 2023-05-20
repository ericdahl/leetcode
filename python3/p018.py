class Solution:

    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()

        result = set()

        for a in range(len(nums)):

            for b in range(a + 1, len(nums) - 2):
                left = b + 1
                right = len(nums) - 1

                while left < right:

                    t = (nums[b], nums[a], nums[left], nums[right])
                    s = sum(t)

                    if s == target:
                        result.add(t)
                        left += 1
                    elif s < target:
                        left += 1
                    else:
                        right -= 1

        return result

