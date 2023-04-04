class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # create a result_list to store the result
        result_list = [[]]
        # create a recursive function to generate all subsets
        def recursive_subset(result_list, instant_combination, nums, max_size):
            # if the length of the instant_combination is equal to the max_size, this is base case and return
            if len(instant_combination) == max_size:
                return
            # iterate over the nums list
            for i in range(len(nums)):
                # if the list is empty or the list is not empty and the last element of the list is less than the current element
                if len(instant_combination) == 0 or (len(instant_combination) != 0 and instant_combination[-1] <= nums[i]):
                    # append the instant_combination + [nums[i]] to the result_list
                    if instant_combination + [nums[i]] not in result_list:
                        result_list.append(instant_combination + [nums[i]])
                    # append the nums[i] to the instant_combination
                    instant_combination.append(nums[i])
                    # create a tmp_nums to store the nums list without the nums[i]
                    tmp_nums = nums.copy()
                    tmp_nums.remove(nums[i])
                    # call the recursive_subset function
                    recursive_subset(result_list, instant_combination, tmp_nums, max_size)
                    # remove the last element of the instant_combination
                    instant_combination.remove(nums[i])

        # call the recursive_subset function
        recursive_subset(result_list, [], nums, len(nums))
        # return the result_list
        return result_list