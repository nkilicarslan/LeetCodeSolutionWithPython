class Solution:
from typing import List
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        memoization_dp = {}
        def findMinPath(x, y):
            if (x,y) in memoization_dp:
                return memoization_dp[(x,y)]
            elif x == len(grid)-1 and y == len(grid[0])-1:
                return grid[x][y]
            elif y == len(grid[0])-1:
                memoization_dp[(x, y)] = findMinPath(x + 1, y) + grid[x][y]
                return memoization_dp[(x, y)]
            elif x == len(grid)-1:
                memoization_dp[(x, y)] = findMinPath(x, y + 1) + grid[x][y]
                return memoization_dp[(x, y)]
            else:
                memoization_dp[(x, y)] = min(findMinPath(x + 1, y), findMinPath(x, y + 1)) + grid[x][y]
                return memoization_dp[(x, y)]

        return findMinPath(0, 0)


