from typing import List
class Solution:
    # this function will merge the nums1 and nums2 into nums1
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # create a final_arr to store the final array
        final_arr = []
        # create two variables to store the index of the nums1 and nums2
        index1 = 0
        index2 = 0
        # iterate over the nums1 and nums2
        while index1 < m and index2 < n:
            # if the current element of nums1 is less than the current element of nums2
            if nums1[index1] < nums2[index2]:
                # append the current element of nums1 to the final_arr and increment the index1
                final_arr.append(nums1[index1])
                index1 += 1
            # otherwise
            else:
                # append the current element of nums2 to the final_arr and increment the index2
                final_arr.append(nums2[index2])
                index2 += 1
        # if the index1 is equal to the length of the nums1 update the final_arr with the rest of the nums2
        if index1 == m:
            final_arr = final_arr + nums2[index2:]
        # if the index2 is equal to the length of the nums2 update the final_arr with the rest of the nums1
        else:
            final_arr = final_arr + nums1[index1:m]
        # iterate over the range of the length of the final_arr and update the nums1
        for i in range(m+n):
            nums1[i] = final_arr[i]
