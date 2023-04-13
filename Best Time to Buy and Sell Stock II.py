from typing import List
class Solution:
    # this function will return the maximum profit that can be made
    def maxProfit(self, prices: List[int]) -> int:
        # create variables to store the maximum count, profit, left_ptr and right_ptr
        max_count = 0
        profit = 0
        left_ptr = 99999
        right_ptr = 99999
        # iterate over the range of the length of the prices list
        for i in range(0,len(prices)):
            # if the current price is less than the left_ptr
            if prices[i] < right_ptr:
                # update the profit with the difference of the right_ptr and left_ptr, update the left_ptr and right_ptr
                profit += right_ptr - left_ptr
                left_ptr = prices[i]
                right_ptr = prices[i]
            # otherwise
            else:
                # check if the current price is greater than the right_ptr, if so update the right_ptr
                if prices[i] > right_ptr:
                    right_ptr = prices[i]
        # at the end check if the right_ptr - left_ptr is greater than 0, if so update the profit
        if right_ptr - left_ptr > 0:
            profit += right_ptr - left_ptr
        return profit
