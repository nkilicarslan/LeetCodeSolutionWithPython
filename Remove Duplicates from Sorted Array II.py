from typing import List
class Solution:
    # This function will remove some duplicates in-place such that each unique element appears at most twice
    def removeDuplicates(self, nums: List[int]) -> int:
        # create a variable to store the occurence count
        occurence_count = 1
        # create a variable to store the index of the loop
        index = 0
        # iterate over the nums list
        while index < len(nums)-1:
            # if the current element is equal to the next element
            if nums[index] == nums[index+1]:
                # increment the occurence_count
                occurence_count += 1
                # if the occurence_count is greater than 2
                if occurence_count > 2:
                    # delete the current element
                    del nums[index]
                    # decrement the index and continue
                    occurence_count -= 1
                    continue
            # else, set the occurence_count to 1
            else:
                occurence_count = 1
            # increment the index
            index += 1
