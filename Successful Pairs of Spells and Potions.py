from typing import List
class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        result_array = []
        potions.sort()

        for value in spells:
            left_ptr = 0
            right_ptr = len(potions) - 1
            index = len(potions)

            while left_ptr <= right_ptr:
                middle_point = (left_ptr + right_ptr) // 2
                if value * potions[middle_point] >= success:
                    right_ptr = middle_point - 1
                    index = middle_point
                else:
                    left_ptr = middle_point + 1
            result_array.append(len(potions) - index)
        return result_array
