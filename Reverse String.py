class Solution:
    # this function will reverse the string with inplace method
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # create a variable to store the total length of the string
        total_length_of_s = len(s)
        # create a variable to store the half length of the string
        half_length_of_string = total_length_of_s // 2
        # iterate over the range of the half length of the string
        for i in range(half_length_of_string):
            # create a variable to store the temporary value
            tmp_value = s[i]
            # swap the current character with the character from the end of the string
            s[i] = s[total_length_of_s - i - 1]
            # swap the character from the end of the string with the current character
            s[total_length_of_s - i - 1] = tmp_value
