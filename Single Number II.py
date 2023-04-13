class Solution:
    # this function will return the number that appears only once
    def singleNumber(self, nums: List[int]) -> int:
        # create a dictionary to store the number and the count
        dict_for_nums = {}
        # iterate over the list and store the count of each number in the dictionary
        for number in nums:
            # if the number is not in the dictionary, add the number to the dictionary
            if number not in dict_for_nums:
                dict_for_nums[number] = 1
            # otherwise increment the count of the number
            else:
                dict_for_nums[number] = dict_for_nums[number] + 1
        # iterate over the dictionary and return the number that appears only once
        for key, value in dict_for_nums.items():
            if value == 1:
                return key
