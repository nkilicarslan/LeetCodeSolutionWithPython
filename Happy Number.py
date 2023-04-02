class Solution:
    def isHappy(self, n: int) -> bool:
        # create a dictionary to store the number and the sum of the squares of the digits
        dict_for_num = {}
        # iterate until the number is found to be happy or not
        while(True):
            # create a variable to store the sum of the squares of the digits
            squared_sum = 0
            # iterate over the digits of the number
            for i in str(n):
                # add the square of the digit to the squared_sum
                squared_sum += pow(int(i),2)
            # if the squared_sum is 1 return True
            if squared_sum == 1:
                return True
            # if the squared_sum is not in the dict_for_num, add the number to the dictionary
            if squared_sum not in dict_for_num:
                dict_for_num[n] = squared_sum
            # otherwise return False
            else:
                return False
            # update the number
            n = squared_sum
