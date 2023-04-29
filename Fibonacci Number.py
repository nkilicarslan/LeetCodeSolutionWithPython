class Solution:
    # this function will return the nth fibonacci number
    def fib(self, n: int) -> int:
        # if n is 0, return 0
        if n == 0:
            return 0
        # if n is 1, return 1
        if n == 1:
            return 1
        # if n is greater than 1, return the nth fibonacci number
        else:
            # create two variables to store the first and second fibonacci number
            first_val = 0
            second_val = 1
            # iterate n-1 times
            for i in range(n-1):
                # update the first and second fibonacci number
                first_val, second_val = second_val, first_val + second_val
            # return the second fibonacci number
            return second_val
