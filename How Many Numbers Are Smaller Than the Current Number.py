class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        dp_arr = {}
        res_arr = []
        for num in nums:
            if num not in dp_arr:
                dp_arr[num] = 1
            else:
                dp_arr[num] += 1
        for num in nums:
            # take the value from the dictionary which is key is less than the num
            res_arr.append(sum([dp_arr[i] for i in dp_arr if i < num]))
        return res_arr