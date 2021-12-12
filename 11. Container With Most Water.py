from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_val = -1
        left = 0
        right=len(height)-1
        while left < right:
            area = min(height[left],height[right])*(right-left)
            max_val = max(max_val,area)
            if height[left]>height[right]:
                right-=1
            else:
                left +=1
        return max_val