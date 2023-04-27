from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1
        middle = (start + end) // 2
        while start < end:
            if nums[middle] == target:
                return middle
            elif nums[middle] < target:
                start = middle + 1
                middle = (start + end) // 2
            else:
                end = middle - 1
                middle = (start + end) // 2
        return -1
a = Solution()
a.search([-1,0,3,5,9,12], 2)