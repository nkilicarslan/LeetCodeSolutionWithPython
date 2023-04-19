from typing import List
class Solution:
    # this function will return the index of the pivot
    def pivotIndex(self, nums: List[int]) -> int:
        # create a variable to store the left sum
        left_sum = 0
        # create a variable to store the right sum
        right_sum = sum(nums)
        # create a variable to store the previous value
        previous_value = 0
        # iterate over the range of the length of the nums
        for index in range(len(nums)):
            # add the previous value to the left sum
            left_sum += previous_value
            # subtract the current value from the right sum
            right_sum -= nums[index]
            # update the previous value
            previous_value = nums[index]
            # if the left sum is equal to the right sum, return the index
            if left_sum == right_sum:
                return index
        # if the pivot index is not found, return -1
        return -1
