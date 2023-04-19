class Solution:
    # this function will return the maximum wealth that the richest customer has
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        # create a variable to store the total sum
        total_sum = 0
        # iterate over the lists in the accounts
        for list in accounts:
            # create a variable to store the sum of the list
            sum_list = sum(list)
            # if the sum of the list is greater than the total_sum, update the total_sum
            if sum_list > total_sum:
                # update the total_sum
                total_sum = sum_list
        # return the total_sum
        return total_sum
