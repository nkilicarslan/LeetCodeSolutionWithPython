class Solution:
    def addDigits(self, num: int) -> int:
        # if the number is 0, return 0
        if num == 0:
            return 0
        # if the number is divisible by 9, return 9
        elif num % 9 == 0:
            return 9
        # otherwise return the remainder of the number divided by 9
        else:
            return num % 9
