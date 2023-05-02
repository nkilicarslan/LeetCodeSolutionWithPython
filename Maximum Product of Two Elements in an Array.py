class Solution:
    # this function will return the maximum product of two distinct numbers in nums
    def maxProduct(self, nums: List[int]) -> int:
        # find the maximum value in the nums array
        max_value = max(nums)
        # remove the maximum value from the nums array
        del nums[nums.index(max_value)]
        # find the second maximum value in the nums array
        second_max = max(nums)
        # return the maximum product of two distinct numbers in nums
        return (max_value - 1) * (second_max - 1)
