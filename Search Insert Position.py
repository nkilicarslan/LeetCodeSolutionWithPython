from typing import List
class Solution:
    # this function will return the index of the target
    def searchInsert(self, nums: List[int], target: int) -> int:
        # create a start, end, middle variable to store the start, end and middle index of the list
        start = 0
        end = len(nums) - 1
        middle = (start + end) // 2
        # iterate over the list
        while start < end:
            # if the current element is equal to the target return the middle index
            if nums[middle] == target:
                return middle
            # else if the current element is less than the target update the start index
            elif nums[middle] < target:
                start = middle + 1
            # else if the current element is greater than the target update the end index
            elif nums[middle] > target:
                end = middle - 1
            # update the middle index
            middle = (start + end) // 2
        # if the value at the start index is less than the target return the value of start + 1
        if nums[start] < target:
            return start + 1
        # otherwise return the value of start
        else:
            return start
