class Solution:
    # this function will return the shuffled array
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        # create a variable to store the result array
        res_arr = []
        # iterate over the range of n
        for i in range(n):
            # append the nums[i] and nums[i+n] to the res_arr
            res_arr.append(nums[i])
            res_arr.append(nums[i+n])
        # return the res_arr
        return res_arr
