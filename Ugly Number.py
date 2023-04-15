class Solution:
    # this function will return true if the number is a positive integer whose prime factors are limited to 2, 3, and 5.
    def isUgly(self, n: int) -> bool:
        # if the number is negative or 0, return False
        if n <= 0:
            return False
        # iterate until the number is found to be ugly or not
        while(True):
            # if the number is 1, return True
            if n == 1:
                return True
            # if the number is divisible by [2,3,5], divide the number by the divisor
            else:
                is_divisible = False
                for i in [2,3,5]:
                    if n % i == 0:
                        is_divisible = True
                        n = n // i
                # if the number is not divisible by [2,3,5], return False
                if is_divisible == False:
                    return False
