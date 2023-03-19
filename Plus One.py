from typing import List
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # create a list to store the result
        result_arr = []
        # create a variable to store the string representation of the digits
        string_rep_of_digits = ''
        # iterate over the digits list
        for i in range(len(digits)):
            # add the current digit to the string representation of the digits
           string_rep_of_digits = string_rep_of_digits + str(digits[i])
        # convert the string representation of the digits to int
        int_rep_of_digits = int(string_rep_of_digits) + 1
        # iterate over the string representation of the digits
        for i in str(int_rep_of_digits):
            # append the current digit to the result list
            result_arr.append(int(i))
        # return the result list
        return result_arr
