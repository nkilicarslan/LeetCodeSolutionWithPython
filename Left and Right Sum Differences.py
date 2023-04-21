from typing import List
class Solution:
    def leftRigthDifference(self, nums: List[int]) -> List[int]:
        left_sum = []
        right_sum = []
        res_arr = []
        for i in range(len(nums)):
            if i == 0:
                left_sum.append(0)
            else:
                left_sum.append(left_sum[-1] + nums[i-1])
        for i in range(len(nums)-1,-1,-1):
            if i == len(nums) - 1:
                right_sum.append(0)
            else:
                right_sum.append(right_sum[-1] + nums[i+1])
        right_sum = right_sum[::-1]
        for i in range(len(left_sum)):
            res_arr.append(abs(left_sum[i] - right_sum[i]))
        return res_arr
a = Solution()
a.leftRigthDifference([10,4,8,3])