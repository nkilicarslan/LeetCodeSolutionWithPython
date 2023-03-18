class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # create a variable to store the result
        result = 0
        # iterate through the nums
        for i in nums:
            # XOR the result with the current number
            result ^= i
        # return the result
        return result
