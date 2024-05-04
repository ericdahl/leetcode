class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        nums = [int(token) for token in s.split(" ") if token.isdigit()]
        
        last = nums[0]
        for n in nums[1:]:
            if n <= last:
                return False
            last = n
        return True
