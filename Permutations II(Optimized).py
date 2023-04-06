from typing import List
class Solution:
    # this function will return the permutations of the given array
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        # create a res_array to store the result
        res_array = []
        nums_length = len(nums)
        # create a hashmap to store the frequency of the elements
        hashmap = {i:0 for i in nums}
        for i in nums:
            hashmap[i] += 1
        # create a recursive helper function to recursively find the permutations
        def dfs(instant_combination):
            # check the length of the instant combination if holds the condition, append it to the res_array
            if len(instant_combination) == nums_length:
                res_array.append(instant_combination.copy())
            # otherwise
            else:
                # iterate over the hashmap if the hash value is greater than 0, append the key to the instant_combination
                # call the recursive helper function
                for key in hashmap:
                    if hashmap[key] > 0:
                        instant_combination.append(key)
                        hashmap[key] -= 1

                        dfs(instant_combination)
                        instant_combination.pop()
                        hashmap[key] += 1
        # call the recursive helper function
        dfs([])
        return res_array
