from typing import List
class Solution:
    # this solution is solves the problem in O(n) time and O(1) space in buttom up approach
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # iterate over the cost list in reverse order
        for i in range(len(cost)-3,-1,-1):
            # update the cost list with the minimum cost
            cost[i] += min(cost[i+1], cost[i+2])
        # return the minimum cost from the first and second element of the cost list
        return min(cost[0],cost[1])
