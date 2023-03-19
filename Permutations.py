from typing import List
class Solution:
    # this function will return all the permutations of the list
    def permute(self, nums: List[int]) -> List[List[int]]:
        # create a list to store the permutations
        result_list = []
        # create a function to generate the permutations recursively
        def helper_recursive(result_list, nums, permutation):
            # if the length of the nums list is 1 then append the permutation list with the current number, thats means that we have reached the base case
            if len(nums) == 1:
                # append the permutation list with the current number
                result_list.append(permutation + [nums[0]])
                # just return it
                return
            # iterate over the range of the length of the nums list
            for i in range(len(nums)):
                # append the current number to the permutation list
                permutation.append(nums[i])
                # create a copy of the nums list
                tmp_nums = nums.copy()
                # remove the current number from the copy of the nums list
                tmp_nums.remove(nums[i])
                # call the helper_recursive function with the result_list, the copy of the nums list and the permutation list
                helper_recursive(result_list, tmp_nums, permutation)
                # remove the current number from the permutation list
                permutation.remove(nums[i])
        # call the helper_recursive function with the result_list, the nums list and an empty list
        helper_recursive(result_list, nums, [])
        # return the result_list
        return result_list
