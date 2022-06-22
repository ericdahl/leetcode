class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:

        closest_difference = 2**31
        closest_difference_sum = None

        nums.sort()

        # TODO: optimize speed more
        for i in range(len(nums)):
            j = i + 1
            k = len(nums) - 1

            while j < k:
                s = nums[i] + nums[j] + nums[k]

                difference = abs(target - s)

                if difference == 0:
                    return s

                if difference < closest_difference:
                    closest_difference = difference
                    closest_difference_sum = s

                if s < target:
                    j += 1
                else:
                    k -= 1


        return closest_difference_sum