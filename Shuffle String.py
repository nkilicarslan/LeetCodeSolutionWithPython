class Solution:
    # this function will return the shuffled string
    def restoreString(self, s: str, indices: List[int]) -> str:
        # create a variable to store the length of the string
        string_length = len(s)
        # create a variable to store the result string
        result_str = ''
        # iterate over the range of the string length
        for i in range(string_length):
            # add the character at the index of the indices list to the result string
            result_str += s[indices.index(i)]
        # return the result string
        return result_str
