from typing import List
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # create a variable to store the number of rows
        M = len(obstacleGrid)
        # create a variable to store the number of columns
        N = len(obstacleGrid[0])
        # create a variable to store the number of paths
        row = [0] * N
        # set the last element of the row to 1
        row[-1] = 1
        # iterate over the row in reverse order
        for index in range(N-1,-1,-1):
            # if the element is 1, set the element to 0
            if obstacleGrid[-1][index] == 1:
                row[index] = 0
            # otherwise if the index is less than the length of the row - 1 set the element to the next element
            elif index < N - 1:
                row[index] = row[index+1]
        # iterate over the rows in reverse order
        for r in reversed(range(M-1)):
            # create a new row to store the new row
            new_row = [0] * N
            # set the last element of the new row to the last element of the row
            new_row[-1] = row[-1]
            # iterate over the columns in reverse order
            for c in reversed(range(N)):
                # if the element is 1, set the element to 0
                if obstacleGrid[r][c] == 1:
                    new_row[c] = 0
                # otherwise if the column is less than the length of the row - 1, set the element to the sum of the element and the next element
                elif c < N -1:
                    new_row[c] = row[c] + new_row[c+1]
            # update the row
            row = new_row
        # return the first element of the row
        return row[0]
