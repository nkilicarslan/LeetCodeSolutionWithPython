class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # create an dp_array to store the minimum path sum for each row
        dp_array = [0 for i in range(len(triangle) + 2)]
        # iterate over the triangle in reverse order
        for row in triangle[::-1]:
            # iterate over the row
            for index, value in enumerate(row):
                # set the current element of the dp_array to the minimum of the current element and the next element added to the value
                dp_array[index] = value + min(dp_array[index], dp_array[index+1])
        # return the sum
        return dp_array[0]
