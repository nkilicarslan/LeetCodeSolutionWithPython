class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        number_dp = {}
        for i in range(len(nums)):
            if nums[i] not in number_dp:
                number_dp[nums[i]] = [i]
            else:
                number_dp[nums[i]].append(i)
        # iterate over the dictionary values
        for values in number_dp.values():
            # if the values are less than k, return True
            if len(values) > 1:
                for i in range(len(values)-1):
                    if values[i+1] - values[i] <= k:
                        return True

        return False
