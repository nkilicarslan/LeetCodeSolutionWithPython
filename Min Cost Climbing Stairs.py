from typing import List
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp_memoization = {}
        def recursivesolver(index):
            if index in dp_memoization:
                return dp_memoization[index]
            if index >= len(cost):
                return 0
            dp_memoization[index] =  min(cost[index] + recursivesolver(index + 1), cost[index] + recursivesolver(index + 2))
            return dp_memoization[index]
        return min(recursivesolver(0),recursivesolver(1))

a = Solution()
a.minCostClimbingStairs([10,15,20])