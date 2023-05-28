import sys
class Solution:
    # this function will return the maximum possible sum of any pair of elements.
    def minPairSum(self, nums: List[int]) -> int:
        # sort the array
        nums.sort()
        # create a variable to store the maximum sum
        max_num = -sys.maxsize -1
        # iterate over the array and find the maximum sum
        for i in range(len(nums)//2):
            # if the sum is greater than the max_num, update the max_num
            if(nums[i] + nums[-i-1] > max_num):
                max_num = nums[i] + nums[-i-1]
        # return the max_num
        return max_num