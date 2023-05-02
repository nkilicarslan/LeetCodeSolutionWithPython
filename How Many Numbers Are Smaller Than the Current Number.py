class Solution:
    # this function will return an array answer such that answer[i] is the number of elements that are strictly smaller than nums[i].
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        # create a dictionary to store the number
        dp_arr = {}
        # create an array to store the result
        res_arr = []
        # iterate over the nums array
        for num in nums:
            # if the number is not in the dictionary, add the number to the dictionary
            if num not in dp_arr:
                dp_arr[num] = 1
            # otherwise increment the value of the number
            else:
                dp_arr[num] += 1
        # iterate over the nums array
        for num in nums:
            # take the value from the dictionary which is key is less than the num
            res_arr.append(sum([dp_arr[i] for i in dp_arr if i < num]))
        # return the result array
        return res_arr
