# We can solve it by two nested loops instead of 3 nested loops
from typing import List
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest_sum = -10000
        right_index = len(nums)-1
        print("sdfsd")
        for starting_index in range(len(nums)-3):
            left_index = starting_index+1
            while(left_index<right_index):
                instant_sum = nums[starting_index]+nums[left_index]+nums[right_index]
                if instant_sum == target:
                    return target
                if abs(instant_sum-target)<abs(closest_sum-target):
                    closest_sum = instant_sum
                if instant_sum < target:
                    left_index += 1
                else:
                    right_index -= 1
        return closest_sum
a = Solution()
a.threeSumClosest([-1,2,1,-4],1)