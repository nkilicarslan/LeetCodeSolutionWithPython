class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        # if the numRows is 1 return [1]
        if rowIndex == 0:
            return [1]
        # if the numRows is 2 return [1,1]]
        elif rowIndex == 1:
            return [1, 1]
        # if the numRows is greater than 2
        else:
            # create a pascal_array to store the pascal's triangle
            pascal_array = [[1], [1, 1]]
            # iterate over the range of numRows - 1
            for i in range(rowIndex - 1):
                # create a curr_row to store the current row
                curr_row = [1]
                # iterate over the previous row
                for j in range(len(pascal_array[-1]) - 1):
                    # append the sum of the previous row's current element and the next element to the curr_row
                    curr_row.append(pascal_array[-1][j] + pascal_array[-1][j + 1])
                # append the 1 to the curr_row
                curr_row.append(1)
                # append the curr_row to the pascal_array
                pascal_array.append(curr_row)
        # return the rowIndex of the pascal_array
        return pascal_array[rowIndex]