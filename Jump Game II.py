class Solution:
    # this function will return the minimum number of jumps to reach the last index
    def jump(self, nums: List[int]) -> int:
        # create a variable to store the total number of moves
        total_move = 0
        # create a variable to store the farthest distance without move
        farthest_dist_without_token = 0
        # create a variable to store the farthest distance with move
        farthest_dist_with_token = 0
        # iterate over the range of the length of the nums list - 1
        for i in range(len(nums)-1):
            # set the farthest_dist_without_token to the max of the farthest_dist_without_token and the current index + the current number
            farthest_dist_without_token = max(farthest_dist_without_token, i + nums[i])
            # if the farthest_dist_without_token is greater than or equal to the length of the nums list - 1
            if farthest_dist_without_token >= len(nums) - 1:
                # return the total_move + 1
                return total_move + 1
            # if the current index is equal to the farthest_dist_with_token
            elif i == farthest_dist_with_token:
                # increment the total_move by 1
                total_move += 1
                # set the farthest_dist_with_token to the farthest_dist_without_token
                farthest_dist_with_token = farthest_dist_without_token
        # return the total_move
        return total_move