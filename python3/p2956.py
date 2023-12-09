class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:

        s1 = set(nums1)
        s2 = set(nums2)

        counts = [0, 0]

        for val in nums1:
            if val in nums2:
                counts[0] += 1

        for val in nums2:
            if val in nums1:
                counts[1] += 1

        return counts