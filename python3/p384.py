class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def reset(self) -> List[int]:
        return self.nums

    def shuffle(self) -> List[int]:
        nums_copy = self.nums[:]
        shuffled = []
        while nums_copy:
            shuffled.append(nums_copy.pop(randint(0, len(nums_copy) - 1)))
        return shuffled



# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()