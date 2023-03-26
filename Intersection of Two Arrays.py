class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # create a set to store the result
        result_set = set()
        # iterate over the nums1
        for i in nums1:
            # if the current element of the nums1 is in the nums2
            if i in nums2:
                # add the current element of the nums1 to the result_set
                result_set.add(i)
        # return the result_set
        return result_set