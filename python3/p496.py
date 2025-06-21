class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []


        for n1 in nums1:
            next_greatest = -1
            for n2 in nums2[nums2.index(n1):]:
                if n2 > n1:
                    next_greatest = n2
                    break
            result.append(next_greatest)

        return result