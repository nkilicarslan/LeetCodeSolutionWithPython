class Solution:
    # this function will return the sum of all the multiples of 3, 5 or 7 below n
    def sumOfMultiples(self, n: int) -> int:
        # create a variable to store the sum
        sum = 0
        # iterate over the range of n
        for i in range(n+1):
            # if the number is divisible by 3, 5 or 7, add the number to the sum
            if i % 3 == 0 or i % 5 == 0 or i % 7 == 0:
                sum += i
        # return the sum
        return sum
