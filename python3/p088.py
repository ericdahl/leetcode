class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1_subset = nums1[0:m]

        nums1.clear()
        nums1 += nums1_subset + nums2
        nums1.sort()