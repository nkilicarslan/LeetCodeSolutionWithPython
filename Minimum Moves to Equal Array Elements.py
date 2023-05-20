class Solution:
    def minMoves(self, nums: List[int]) -> int:
        number_of_moves = 0
        min_num = min(nums)
        for num in nums:
            number_of_moves += num - min_num
        return number_of_moves
