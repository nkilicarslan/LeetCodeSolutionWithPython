from typing import List
class Solution:
    # this function will rotate the array to the right by k steps
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # if the k value is greater than the length of the nums,
        # then the k value will be the remainder of the k value divided by the length of the nums
        rotate_time = k % len(nums)
        # create a list to store the rotated list
        rotated_list = []
        # iterate over the range of the rotate_time
        for i in range(rotate_time):
            # set the last value of the nums to the last_value
            last_value = nums[-1]
            # delete the last element of the nums
            del nums[-1]
            # append the last_value to the rotated_list
            rotated_list.append(last_value)
        # iterate over the rotated_list and insert the element to the beginning of the nums
        for i in range(len(rotated_list)):
            nums.insert(0,rotated_list[i])
