class Solution:

    @staticmethod
    def compute_gcd(x, y):
        while y:
            x, y = y, x % y
        return x

    @staticmethod
    def find_gcd(nums: List[int]) -> int:
        current_gcd = nums[0]
        for n in nums[1:]:
            current_gcd = Solution.compute_gcd(current_gcd, n)
        return current_gcd

    def countDifferentSubsequenceGCDs(self, nums: List[int]) -> int:

        max_num = max(nums)
        present = [False] * (max_num + 1)
        for num in nums:
            present[num] = True

        result = 0
        for gcd in range(1, max_num + 1):
            common_gcd = 0
            for multiple in range(gcd, max_num + 1, gcd):
                if present[multiple]:
                    common_gcd = Solution.compute_gcd(common_gcd, multiple)
                if common_gcd == gcd:
                    result += 1
                    break

        return result
