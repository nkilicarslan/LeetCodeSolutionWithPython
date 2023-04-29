class Solution:
    # this function will return the number of unique paths in buttom up approach
    def uniquePaths(self, m: int, n: int) -> int:
        # create a variable to store the count of unique paths
        count = 0
        # create a row to store the number of unique paths for a single row
        row = [1] * m
        # iterate n-1 times
        for i in range(n-1):
            # create new row to store the number of unique paths for a single row
            new_row = [1] * m
            # iterate m-1 times
            for j in range(1,m):
                # update the new row with the number of unique paths
                new_row[j] = row[j] + new_row[j-1]
            # assign the new row to the row
            row = new_row
        # return the last element of the row
        return row[len(row)-1]
