class Solution:
    def addDigits(self, num: int) -> int:
        # iterate over the number until the number is less than 10
        while num > 9:
            # create a variable to store the sum of the digits
            sum = 0
            # iterate over the digits of the number
            for i in str(num):
                # add the digit to the sum
                sum += int(i)
            # update the number
            num = sum
        # return the number
        return num
