from typing import List
class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        # create an array to store the result
        result_array = []
        # sort the potions list
        potions.sort()
        # iterate over the spells list
        for value in spells:
            # create a left_ptr and right_ptr to store the left and right pointers
            left_ptr = 0
            right_ptr = len(potions) - 1
            # create an index to store the index of the last successive position of the list
            index = len(potions)
            # iterate over the potions list
            while left_ptr <= right_ptr:
                # calculate the middle point
                middle_point = (left_ptr + right_ptr) // 2
                # if the middle point times the value is greater than or equal to the success
                if value * potions[middle_point] >= success:
                    # update the right_ptr and index
                    right_ptr = middle_point - 1
                    index = middle_point
                # otherwise update the left_ptr
                else:
                    left_ptr = middle_point + 1
            # finally append the calculated value to the result_array
            result_array.append(len(potions) - index)
        # return the result_array
        return result_array
