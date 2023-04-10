class Solution:
    # this function returns the length of the longest consecutive sequence
    def longestConsecutive(self, nums: List[int]) -> int:
        # if the list is empty return 0
        if len(nums) == 0:
            return 0
        # sort the list
        nums.sort()
        count = 1
        min_val = -1
        # iterate over the list and find the longest consecutive sequence
        for i in range(len(nums) - 1):
            # if the current element is equal to the next element + 1 then increment the count
            if nums[i] == nums[i + 1] - 1:
                count += 1
                # if the count is greater than the min_val then update the min_val
                if count > min_val:
                    min_val = count
            # if the current element is equal to the next element then continue
            elif nums[i] == nums[i + 1]:
                continue
            # otherwise reset the count
            else:
                count = 1
        # if the count is greater than the min_val then update the min_val
        if count > min_val:
            min_val = count
        return min_val
