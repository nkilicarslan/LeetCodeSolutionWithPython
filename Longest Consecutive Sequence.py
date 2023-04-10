class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        nums.sort()
        count = 1
        min_val = -1
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1] - 1:
                count += 1
                if count > min_val:
                    min_val = count
            elif nums[i] == nums[i + 1]:
                continue
            else:
                count = 1
        if count > min_val:
            min_val = count
        return min_val

