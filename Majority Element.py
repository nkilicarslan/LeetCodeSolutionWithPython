class Solution:
    # this function will return the majority element of the list
    def majorityElement(self, nums: List[int]) -> int:
        # create a dict to store the number of occurrences of each number
        dict_for_nums = {}
        # iterate over the nums list
        for i in nums:
            # if the current number is in the dict_for_nums
            if i in dict_for_nums:
                # increase the value of the current number by 1
                dict_for_nums[i] += 1
            # if the current number is not in the dict_for_nums
            else:
                # add the current number to the dict_for_nums with the value of 1
                dict_for_nums[i] = 1
        # return the maximum value of the dict_for_nums
        return max(dict_for_nums, key=dict_for_nums.get)
