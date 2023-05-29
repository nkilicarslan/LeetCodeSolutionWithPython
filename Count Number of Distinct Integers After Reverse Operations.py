class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        dict_of_distinct_nums = {}
        distinct_sum = 0
        for num in nums:
            if num not in dict_of_distinct_nums:
                dict_of_distinct_nums[num] = 1

        distinct_sum += len(dict_of_distinct_nums.keys())

        for num in nums:
            num = int(str(num)[::-1])
            if num not in dict_of_distinct_nums:
                dict_of_distinct_nums[num] = 1
                distinct_sum += 1

        return distinct_sum
