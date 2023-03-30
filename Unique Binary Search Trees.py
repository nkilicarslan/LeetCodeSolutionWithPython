class Solution:
    # this function will return the number of unique binary search trees
    def numTrees(self, n: int) -> int:
        # create a dp array to store the number of unique binary search trees for each number
        dp_array_for_nums = [1 for i in range(n+1)]
        # iterate over the for loop from 2 to n
        for i in range(2,n + 1):
            # create a total_count variable to store the total number of unique binary search trees
            total_count = 0
            # iterate over the range of i
            for j in range(0,i):
                # get the left and right pointers
                left_ptr = j
                right_ptr = i - j - 1
                # increment the total_count by the product of the left and right pointers
                total_count += dp_array_for_nums[left_ptr] * dp_array_for_nums[right_ptr]
            # set the current element of the dp_array_for_nums to the total_count
            dp_array_for_nums[i] = total_count
        # return the last element of the dp_array_for_nums
        return dp_array_for_nums[n]
