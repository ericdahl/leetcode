class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:

        common = Counter(nums1) & Counter(nums2)
        result = []
        for n in common:
            result += [n] * common[n]

        return result