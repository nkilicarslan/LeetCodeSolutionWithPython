class Solution:
    # this function will return the array after partitioning it according to the pivot
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        # create two lists and one variable to store the numbers less than the pivot, equal to the pivot, and more than the pivot
        less_than_pivot = []
        more_than_pivot = []
        equal_to_pivot = 0
        # iterate over the nums
        for num in nums:
            # if the number is less than the pivot, append it to the less_than_pivot list
            if num > pivot:
                more_than_pivot.append(num)
            # if the number is more than the pivot, append it to the more_than_pivot list
            elif num < pivot:
                less_than_pivot.append(num)
            # if the number is equal to the pivot, increment the equal_to_pivot variable
            else:
                equal_to_pivot += 1
        # create a list of the pivot
        equal_to_pivot = [pivot for i in range(equal_to_pivot)]
        # return the concatenation of the less_than_pivot, equal_to_pivot, and more_than_pivot lists
        return less_than_pivot + equal_to_pivot + more_than_pivot
