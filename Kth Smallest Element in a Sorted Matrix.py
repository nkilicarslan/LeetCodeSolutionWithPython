class Solution:
    # this function will return the kth smallest element in the matrix
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        # create a list to store all the values of the matrix
        all_values_of_matrix = []
        # iterate over the matrix and add the values to the list
        for list in matrix:
            for value in list:
                # add the value to the list
                all_values_of_matrix.append(value)
        # sort the list
        all_values_of_matrix = sorted(all_values_of_matrix)
        # return the kth smallest element
        return all_values_of_matrix[k-1]
