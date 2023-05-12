from typing import List
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        dict_stones = {}
        sum = 0
        for char in stones:
            if char not in dict_stones:
                dict_stones[char] = 1
            else:
                dict_stones[char] += 1
        for char in jewels:
            if char in dict_stones:
                sum += dict_stones[char]
        return sum

