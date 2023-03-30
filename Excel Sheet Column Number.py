class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        # create a total_count variable to store the total count
        total_count = 0
        # iterate over the given string
        for i in range(len(columnTitle)):
            # get the ascii value of the current element of the columnTitle
            ascii_value = ord(columnTitle[i]) - 64
            # increment the total_count by the product of the total_count and 26 and add the new ascii_value
            total_count = total_count * 26 + ascii_value
        # return the total_count
        return total_count
