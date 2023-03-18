from typing import List
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # create a variable to store the length of the nums
        length_of_the_nums = len(nums)
        # if the length of the nums is 0
        if length_of_the_nums == 0:
            # return the not found result scenario
            return [-1,-1]
        # if the length of the nums is not 0
        else:
            # create a variable to store the min_index
            min_index = -1
            # create a variable to store the max_index
            max_index = -1
            # create a variable to store the iterator_index
            iterator_index = length_of_the_nums//2
            # create a variable to store the left_ptr
            left_ptr = 0
            # create a variable to store the right_ptr
            right_ptr = length_of_the_nums
            # create a while loop to iterate through the nums
            while True:
                # if the iterator_index is equal to the left_ptr or the right_ptr and the nums[iterator_index] is not equal to the target
                if (left_ptr == iterator_index or right_ptr == iterator_index) and nums[iterator_index] != target:
                    # return the not found result scenario
                    return [-1,-1]
                # if the nums[iterator_index] is less than the target
                elif nums[iterator_index] < target:
                    # create a variable to store the tmp_index
                    tmp_index = iterator_index
                    # update the iterator_index
                    iterator_index = (right_ptr + iterator_index) // 2
                    # update the left_ptr
                    left_ptr = tmp_index
                # if the nums[iterator_index] is greater than the target
                elif nums[iterator_index] > target:
                    # create a variable to store the tmp_index
                    tmp_index = iterator_index
                    # update the iterator_index
                    iterator_index = (iterator_index + left_ptr) // 2
                    # update the right_ptr
                    right_ptr = tmp_index
                # if the nums[iterator_index] is equal to the target
                elif nums[iterator_index] == target:
                    # update the min_index
                    min_index = iterator_index
                    # update the max_index
                    max_index = iterator_index
                    # create a while loop to iterate through the nums
                    while True:
                        # create a variable to store the flag_min
                        flag_min = True
                        # create a variable to store the flag_max
                        flag_max = True
                        # if the min_index is greater than 0 and the nums[min_index-1] is equal to the target
                        if min_index > 0 and nums[min_index-1] == target:
                            # update the min_index
                            min_index = min_index - 1
                            # set the flag_min to False
                            flag_min = False
                        # if the max_index is less than the length of the nums and the nums[max_index+1] is equal to the target
                        if max_index < len(nums) -1 and nums[max_index+1] == target:
                            # update the max_index
                            max_index = max_index + 1
                            # set the flag_max to False
                            flag_max = False
                        # if the flag_min is True and the flag_max is True, break the loop
                        if flag_min == True and flag_max == True:
                            break
                    # return the found result scenario
                    return [min_index, max_index]
