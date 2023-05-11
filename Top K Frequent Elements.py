class Solution:
    # this function will return the k most frequent elements. You may return the answer in any order.
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # create a dictionary to store the number and the frequency
        dict_values = {}
        # iterate over the numbers
        for num in nums:
            # if the number is not in the dictionary, add the number to the dictionary
            if num not in dict_values:
                dict_values[num] = 1
            # otherwise increment the frequency of the number
            else:
                dict_values[num] += 1
        # sort the dictionary by the frequency of the numbers
        sorted_values = sorted(dict_values.items(), key=lambda x: x[1], reverse=True)
        # return the k most frequent elements
        return [sorted_values[i] for i in range(k)]
