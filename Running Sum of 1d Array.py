class Solution:
    # this function will return the running sum of the array
    def runningSum(self, nums: List[int]) -> List[int]:
        # create a variable to store the total sum
        total_sum = 0
        # create a variable to store the result array
        result_arr = []
        # iterate over the nums
        for num in nums:
            # add the num to the total_sum
            total_sum += num
            # append the total_sum to the result_arr
            result_arr.append(total_sum)
        # return the result_arr
        return result_arr
