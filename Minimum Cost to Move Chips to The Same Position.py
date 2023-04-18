class Solution:
    # this function will return the minimum cost to move all the chips to the same position
    def minCostToMoveChips(self, position: List[int]) -> int:
        # create a variable to store the sum of the even positions
        even_sum = 0
        # create a variable to store the sum of the odd positions
        odd_sum = 0
        # iterate over the positions
        for pos in position:
            # if the position is even, add 1 to the even_sum
            if pos % 2 == 0:
                even_sum += 1
            # otherwise add 1 to the odd_sum
            else:
                odd_sum += 1
        # return the minimum of the even_sum and the odd_sum
        return min(even_sum,odd_sum)
