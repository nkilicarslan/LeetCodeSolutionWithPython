class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        all_values_of_matrix = []
        for list in matrix:
            for value in list:
                all_values_of_matrix.append(value)
        all_values_of_matrix = sorted(all_values_of_matrix)
        return all_values_of_matrix[k-1]
