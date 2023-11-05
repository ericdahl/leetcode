class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:

        nums1_sum = sum(nums1)
        nums2_sum = sum(nums2)

        nums1_zeros = nums1.count(0)
        nums2_zeros = nums2.count(0)

        if nums1_zeros == 0 and nums2_zeros == 0:
            if nums1_sum == nums2_sum:
                return nums1_sum
            return -1

        if nums1_zeros == 0:
            if nums2_sum + nums2_zeros > nums1_sum:
                return -1
            return nums1_sum
        if nums2_zeros == 0:
            if nums1_sum + nums1_zeros > nums2_sum:
                return -1
            return nums2_sum

        if nums1_sum + nums1_zeros > nums2_sum + nums2_zeros:
            return nums1_sum + nums1_zeros

        else:
            return nums2_sum + nums2_zeros

