class Solution:
    # this function will return true if s is a subsequence of t
    def isSubsequence(self, s: str, t: str) -> bool:
        # create a variable to store the length of the string s
        len_s = len(s)
        # create a variable to store the length of the string t
        len_t = len(t)
        # create a variable to store the index of the string s
        index = 0
        # iterate over the string t
        for i in range(len_t):
            # if the index of the string s is equal to the length of the string s, return True
            if index == len_s:
                return True
            # if the character of the string s is equal to the character of the string t, increment the index of the string s
            if s[index] == t[i]:
                index += 1
        # if the index of the string s is equal to the length of the string s, return True
        if index == len_s:
            return True
        # otherwise return False
        return False
