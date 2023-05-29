class Solution:
    # this function will return the number of distinct integers in nums after reversing the digits of the integers.
    def countDistinctIntegers(self, nums: List[int]) -> int:
        # create a dictionary to store the distinct integers
        dict_of_distinct_nums = {}
        # create a variable to store the sum of the distinct integers
        distinct_sum = 0
        # iterate over the nums and add the distinct integers to the dictionary
        for num in nums:
            if num not in dict_of_distinct_nums:
                dict_of_distinct_nums[num] = 1

        # iterate over the dictionary and add the length of the dictionary to the distinct_sum
        distinct_sum += len(dict_of_distinct_nums.keys())

        # iterate over the nums and reverse the digits of the integers
        for num in nums:
            num = int(str(num)[::-1])
            # if the reversed integer is not in the dictionary, add it to the dictionary and add 1 to the distinct_sum
            if num not in dict_of_distinct_nums:
                dict_of_distinct_nums[num] = 1
                distinct_sum += 1

        # return the distinct_sum
        return distinct_sum
