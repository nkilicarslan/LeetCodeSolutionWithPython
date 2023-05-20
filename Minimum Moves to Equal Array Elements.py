class Solution:
    # this function will return the minimum number of moves required to make all array elements equal, where a move consists of incrementing n - 1 elements by 1.
    def minMoves(self, nums: List[int]) -> int:
        # create a variable to store the number of moves
        number_of_moves = 0
        # find the minimum number in the array
        min_num = min(nums)
        # iterate over the array and update the number_of_moves
        for num in nums:
            number_of_moves += num - min_num
        # return the number_of_moves
        return number_of_moves
