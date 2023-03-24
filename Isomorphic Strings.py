class Solution:
    # this function will return True if the two strings are isomorphic and False if they are not
    def isIsomorphic(self, s: str, t: str) -> bool:
        # if the length of the first string is not equal to the length of the second string, return False
        if len(s) != len(t):
            return False
        # create a dictionary to store the index of the first string
        dict_for_first_str = {}
        # create a dictionary to store the index of the second string
        dict_for_second_str = {}
        # create a list to store the index of the first string
        index_list_first = []
        # create a list to store the index of the second string
        index_list_second = []
        # iterate over the range of the length of the strings
        for i in range(len(s)):
            # if the current character of the first string is not in the dictionary
            if s[i] not in dict_for_first_str:
                # add the current character of the first string to the dictionary with the current index as the value
                dict_for_first_str[s[i]] = i
                # add the current index to the index list of the first string
                index_list_first.append(i)
            # if the current character of the first string is in the dictionary
            else:
                # add the value of the current character of the first string to the index list of the first string
                index_list_first.append(dict_for_first_str[s[i]])
            # if the current character of the second string is not in the dictionary
            if t[i] not in dict_for_second_str:
                # add the current character of the second string to the dictionary with the current index as the value
                dict_for_second_str[t[i]] = i
                # add the current index to the index list of the second string
                index_list_second.append(i)
            # if the current character of the second string is in the dictionary
            else:
                # add the value of the current character of the second string to the index list of the second string
                index_list_second.append(dict_for_second_str[t[i]])
        # if both lists are same
        if index_list_first == index_list_second:
            # return True
            return True
        # otherwise return False
        return False
