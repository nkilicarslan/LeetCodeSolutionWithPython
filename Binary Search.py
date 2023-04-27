from typing import List
class Solution:
    # this solution implements binary search to find the target in the sorted array
    def search(self, nums: List[int], target: int) -> int:
        # create a start, end, and middle pointer
        start = 0
        end = len(nums) - 1
        middle = (start + end) // 2
        # iterate until the target is found or the start and end pointers cross
        while start <= end:
            # if the middle value is the target, return the index of the middle value
            if nums[middle] == target:
                return middle
            # if the middle value is less than the target, update the start and middle pointer
            elif nums[middle] < target:
                start = middle + 1
                middle = (start + end) // 2
            # if the middle value is greater than the target, update the end and middle pointer
            else:
                end = middle - 1
                middle = (start + end) // 2
        # if the target is not found, return -1
        return -1
