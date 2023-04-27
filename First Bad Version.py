# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    # this function will return the first bad version of the product, also this function use binary search technique
    def firstBadVersion(self, n: int) -> int:
        # create a start, end, and middle pointer
        start = 0
        end = n
        middle = (start + end) // 2
        # iterate until the start and end pointers cross
        while start <= end:
            # if the isBadVersion(middle) is False, update the start and middle pointer to the right
            if isBadVersion(middle) == False:
                start = middle + 1
                middle = (start + end) // 2
            # if the isBadVersion(middle) is True, update the end and middle pointer to the left
            else:
                end = middle - 1
                middle = (start + end) // 2
        # return the middle pointer + 1
        return middle + 1
