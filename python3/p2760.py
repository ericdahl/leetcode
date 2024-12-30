class Solution:
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        longest = 0

        for l in range(len(nums)):
            if nums[l] % 2 != 0 or nums[l] > threshold:
                continue

            curr_length = 1
            for i in range(l + 1, len(nums)):
                if nums[i] > threshold:
                    break

                if (nums[i] % 2 == nums[i - 1] % 2):
                    break

                curr_length += 1

            longest = max(longest, curr_length)

        return longest