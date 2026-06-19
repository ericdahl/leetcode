class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        k %= len(nums)
        cut = len(nums) - k
        new =  nums[cut:] + nums[:cut]
        for i in range(len(nums)):
            nums[i] = new[i]
