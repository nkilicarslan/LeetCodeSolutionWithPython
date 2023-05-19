class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        less_than_pivot = []
        more_than_pivot = []
        equal_to_pivot = 0
        for num in nums:
            if num > pivot:
                more_than_pivot.append(num)
            elif num < pivot:
                less_than_pivot.append(num)
            else:
                equal_to_pivot += 1
        equal_to_pivot = [pivot for i in range(equal_to_pivot)]
        return less_than_pivot + equal_to_pivot + more_than_pivot