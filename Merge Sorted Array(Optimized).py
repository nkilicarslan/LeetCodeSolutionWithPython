from typing import List
class Solution:
    # this function will merge the nums1 and nums2 into nums1
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # create two variables to store the last index of the nums1 and nums2
        last_index_for_1 = m-1
        last_index_for_2= n-1
        # create a variable to store the last writable index
        last_writable_index = m + n - 1
        # iterate over the nums1 and nums2
        while last_index_for_2 >= 0:
            # if the last index for nums1 is greater than or equal to 0 and the current element of nums1 is greater than the current element of nums2
            if last_index_for_1 >= 0 and nums1[last_index_for_1] > nums2[last_index_for_2]:
                # update the current element of nums1 with the current element of nums1 and decrement the last_index_for_1
                nums1[last_writable_index] = nums1[last_index_for_1]
                last_index_for_1 -= 1
            # otherwise
            else:
                # update the current element of nums1 with the current element of nums2 and decrement the last_index_for_2
                nums1[last_writable_index] = nums2[last_index_for_2]
                last_index_for_2 -= 1
            # decrement the last_writable_index
            last_writable_index -= 1
