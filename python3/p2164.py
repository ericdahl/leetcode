class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        
        even = []
        odd = []
        while nums:
            even.append(nums.pop(0))
            if nums:
                odd.append(nums.pop(0))
            
        odd.sort(reverse=True)
        even.sort()
        
        while even:
            nums.append(even.pop(0))
            if odd:
                nums.append(odd.pop(0))

        return nums
