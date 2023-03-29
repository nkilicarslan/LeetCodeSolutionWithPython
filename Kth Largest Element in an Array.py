from typing import List
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # sort the nums
        nums.sort()
        # return the kth largest element
        return nums[len(nums)- k]
