from typing import List
class Solution:
    def leftRigthDifference(self, nums: List[int]) -> List[int]:
        left_sum = [0]
        right_sum = [sum(nums) - nums[0]]
        res_arr = []
        for i in range(len(nums)):
            if i == 0:
                left_sum.append(left_sum[-1] + nums[i])
            if i == len(nums) -1:
                right_sum.append(right_sum[-1] - nums[i])
            else:
                left_sum.append(left_sum[-1] + nums[i])
                right_sum.append(right_sum[-1] - nums[i])
        for i in range(len(left_sum)):
            res_arr.append(abs(left_sum[i]-right_sum[i]))
        return res_arr

a = Solution()
a.leftRigthDifference([1])