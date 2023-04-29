from typing import List
class Solution:
    # this solution is solves the problem in top-down, memoization approach
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # create a dictionary to store the index and the minimum cost
        dp_memoization = {}
        # create a recursive function to solve the problem
        def recursivesolver(index):
            # if the index is in the dictionary, return the value
            if index in dp_memoization:
                return dp_memoization[index]
            # if the index is greater than or equal to the length of the cost list, return 0
            if index >= len(cost):
                return 0
            # recursively call the function and update the dictionary
            dp_memoization[index] =  min(cost[index] + recursivesolver(index + 1), cost[index] + recursivesolver(index + 2))
            # return the value
            return dp_memoization[index]
        # return the minimum cost from the first and second element of the cost list
        return min(recursivesolver(0),recursivesolver(1))
