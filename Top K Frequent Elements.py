class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict_values = {}
        for num in nums:
            if num not in dict_values:
                dict_values[num] = 1
            else:
                dict_values[num] += 1
        sorted_values = sorted(dict_values.items(), key=lambda x: x[1], reverse=True)
        return [sorted_values[i] for i in range(k)]
