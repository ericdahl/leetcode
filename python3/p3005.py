class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        c = Counter(nums)

        top_freq = -1
        total_top_freq = 0
        for mc in c.most_common():
            if mc[1] < top_freq:
                break

            top_freq = mc[1]            
            total_top_freq += top_freq

        return total_top_freq
