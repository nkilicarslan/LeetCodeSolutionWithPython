from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # create a variable to store deleted_numbers
        deleted_numbers = 0
        # create a variable to store the index of the list
        i = 0
        # create a while loop to iterate through the list
        while i < len(nums) - 1:
            # if the current number is equal to the next number
            if nums[i] == nums[i+1]:
                # delete the current number
                del nums[i]
                # increase the deleted_numbers by 1
                deleted_numbers += 1
            # if the current number is not equal to the next number
            else:
                # increase the index by 1
                i += 1
        # return the length of the list
        return len(nums)

