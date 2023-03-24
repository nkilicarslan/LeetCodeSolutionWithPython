from typing import List
class Solution:
    # this function will return the longest common prefix of the list
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # create a variable to store instantly the first string of the list
        longest_common = strs[0]
        # iterate over the range of the length of the list
        for i in range(1,len(strs)):
            # create a variable to store the instant string
            instant_str = strs[i]
            # create a variable to store the minimum length of the longest_common and the current string
            min_length = min(len(instant_str), len(longest_common))
            # create a variable to store the new common string
            new_common_str = ''
            # iterate over the range of the minimum length
            for j in range(min_length):
                # if the current character of the longest_common is equal to the current character of the current string
                if instant_str[j] == longest_common[j]:
                    # add the current character to the new common string
                    new_common_str += longest_common[j]
                # otherwise break the loop
                else:
                    break
            # set the longest_common to the new common string
            longest_common = new_common_str
        # return the longest_common
        return longest_common
