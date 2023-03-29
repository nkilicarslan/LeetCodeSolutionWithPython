from typing import List
class Solution:
    # this function will sort the colors with inplace method
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        # iterate over the range of the length of the nums
        while i < len(nums):
            # if the current element is 0
            if nums[i] == 0:
                # delete the current element
                del nums[i]
                # insert the current element to the beginning of the list
                nums.insert(0,0)
            # if the current element is 2
            elif nums[i] == 2:
                # delete the current element
                del nums[i]
                # append the current element to the end of the list
                nums.append(2)
                # if the from i to the end of the list is all 2
                if nums[i:] == [2 for i in range(len(nums[i:]))]:
                    # break the loop
                    break
                # decrement the i by 1
                i -= 1
            # increment the i by 1
            i += 1
