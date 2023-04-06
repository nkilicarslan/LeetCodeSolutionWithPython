from typing import List
class Solution:
    # this function will return the permutations of the given array
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        # create a res_array to store the result
        res_array = []
        nums_length = len(nums)
        # create a recursive helper function to recursively find the permutations
        def recursive_helper(instant_combination, num_list):
            # if the instant combination length is equal to the nums length, that means we reached the base case, so append it
            if len(instant_combination) == nums_length:
                if instant_combination not in res_array:
                    res_array.append(instant_combination.copy())
            # otherwise iterate over the num_list and append the current element to the instant_combination and call the recursive helper function
            else:
                for index, elem in enumerate(num_list):
                    instant_combination.append(elem)
                    tmp_nums = num_list.copy()
                    del tmp_nums[index]
                    recursive_helper(instant_combination, tmp_nums)
                    instant_combination.pop()
        # call the recursive helper function
        recursive_helper([], nums)
        return res_array
