import math
class Solution:
    # this function will return the least number of perfect square numbers that sum to n
    def numSquares(self, n: int) -> int:
        # create a variable to store the result
        dp_arr = [n] * (n+1)
        # initialize the first element of the dp_arr to 0
        dp_arr[0] = 0
        # iterate over the range of 1 to n
        for target in range(1,n+1):
            # iterate over the range of 1 to the target
            for num in range(1,target+1):
                # create a variable to store the square of the num
                squared = num * num
                # if the target - squared is less than 0, break
                if target - squared < 0:
                    break
                # update the dp_arr
                dp_arr[target] = min(dp_arr[target], dp_arr[target- squared] + 1)
        # return the last element of the dp_arr
        return dp_arr[n]
