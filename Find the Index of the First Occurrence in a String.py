class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # iterate through the haystack
        for i in range(len(haystack)):
            # if the needle is found in the haystack
            if haystack[i:i+len(needle)] == needle:
                # return the index of the first occurrence
                return i
        # if the needle is not found in the haystack, return -1
        return -1