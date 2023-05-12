from typing import List
class Solution:
    # this function will return the number of jewels in the stones
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        # create a dictionary to store the stones and their count
        dict_stones = {}
        # create a variable to store the sum of the jewels in the stones
        sum = 0
        # iterate over the stones and add the stones to the dictionary
        for char in stones:
            # if the stone is not in the dictionary, add the stone to the dictionary
            if char not in dict_stones:
                dict_stones[char] = 1
            # otherwise increment the count of the stone
            else:
                dict_stones[char] += 1
        # iterate over the jewels and add the count of the jewels in the stones
        for char in jewels:
            # if the jewel is in the dictionary, add the count of the jewel to the sum
            if char in dict_stones:
                sum += dict_stones[char]
        # return the sum
        return sum
