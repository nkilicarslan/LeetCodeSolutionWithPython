import sys
class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        max_num = -sys.maxsize -1
        for i in range(len(nums)//2):
            if(nums[i] + nums[-i-1] > max_num):
                max_num = nums[i] + nums[-i-1]
        return max_num