from typing import List
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # iterate over the last row of the grid
        for i in range(len(grid[0])-2, -1, -1):
            # update the last row of the grid
            grid[-1][i] += grid[-1][i+1]
        # iterate over the last column of the grid
        for i in range(len(grid)-2, -1, -1):
            # update the last column of the grid
            grid[i][-1] += grid[i+1][-1]
        # iterate over the grid
        for i in range(len(grid)-2, -1, -1):
            for j in range(len(grid[0])-2, -1, -1):
                # update the current element of the grid
                grid[i][j] += min(grid[i+1][j], grid[i][j+1])
        # return the first element of the grid
        return grid[0][0]
