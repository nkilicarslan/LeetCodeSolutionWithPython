class Solution:
    # this function will return the summary ranges of the list
    def summaryRanges(self, nums: List[int]) -> List[str]:
        # create a list to store the result
        result_array = []
        # create a variable to store the left range value
        left_val = "-1"
        # create a variable to store the right range value
        right_val = "-1"
        # iterate over the nums list
        for i in range(len(nums)):
            # if the left_val is str(-1)
            if left_val == "-1":
                # set the left_val to the current number
                left_val = nums[i]
            # if the current number is equal to the previous number + 1
            elif nums[i] - nums[i-1] == 1:
                # set the right_val to the current number
                right_val = nums[i]
            # if the difference between the current number and the previous number is not equal to 1
            else:
                # if the right_val is str(-1)
                if right_val == "-1":
                    # append the left_val to the result list
                    result_array.append(str(left_val))
                else:
                    # append the left_val and the right_val to the result list
                    result_array.append(str(left_val) + "->" + str(right_val))
                # set the left_val to the current number
                left_val = nums[i]
                # set the right_val to str(-1)
                right_val = "-1"
        # if the right_val is not str(-1)
        if right_val != "-1":
            # append the left_val and the right_val to the result list
            result_array.append(str(left_val) + "->" + str(right_val))
        # if the left_val is not str(-1)
        elif left_val != "-1":
            # append the left_val to the result list
            result_array.append(str(left_val))
        # return the result list
        return  result_array
