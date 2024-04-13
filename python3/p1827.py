class Solution:
    def minOperations(self, nums: List[int]) -> int:
        
        operations = 0
        last = nums[0]

        for n in nums[1:]:            
            
            if n > last:
                last = n
                continue
            
            operations += abs(n - last) + 1
            last += 1

        return operations
