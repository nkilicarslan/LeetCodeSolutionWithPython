from typing import List
class Solution:
    # this function will return the amount of water that can be trapped
    def trap(self, height: List[int]) -> int:
        # create a list to store the left most minimum value
        left_most_min = [0 for i in range(len(height))]
        # set the first element of the left_most_min to the first element of the height
        left_most_min[0] = height[0]
        # create a list to store the right most minimum value
        right_most_min = [0 for i in range(len(height))]
        # set the last element of the right_most_min to the last element of the height
        right_most_min[-1] = height[-1]
        # create a list to store the minimum value between the left most minimum value and the right most minimum value
        min_left_right_value = [0 for i in range(len(height))]
        # create a variable to store the total amount of water that can be trapped
        res = 0
        # iterate over the range of the length of the height
        for i in range(1,len(height)):
            # set the current element of the left_most_min to the max of the previous element of the left_most_min and the current element of the height
            left_most_min[i] = max(left_most_min[i-1],height[i])
        # iterate over the height list in reverse order
        for i in range(len(height)-2,-1,-1):
            # set the current element of the right_most_min to the max of the next element of the right_most_min and the current element of the height
            right_most_min[i] = max(right_most_min[i+1], height[i])
        # iterate over the range of the length of the height
        for i in range(len(height)):
            # set the current element of the min_left_right_value to the min of the current element of the right_most_min and the current element of the left_most_min
            min_left_right_value[i] = min(right_most_min[i], left_most_min[i])
            # if the current element of the min_left_right_value is greater than the current element of the height
            if min_left_right_value[i] > height[i]:
                # increment the res by the difference between the current element of the min_left_right_value and the current element of the height
                res += min_left_right_value[i] - height[i]
        # return the results
        return res
