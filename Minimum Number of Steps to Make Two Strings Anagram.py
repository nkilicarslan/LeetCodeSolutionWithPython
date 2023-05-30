class Solution:
    # this function will return the minimum number of steps to make s and t anagram
    def minSteps(self, s: str, t: str) -> int:
        # create a variable to store the total count
        total_count = 0
        # create a dictionary to store the count of the characters in s
        dict_for_first_word = {}
        # iterate over the characters in s and add them to the dictionary
        for char in s:
            if char not in dict_for_first_word:
                dict_for_first_word[char] = 1
            # if the character is already in the dictionary, add 1 to the count
            else:
                dict_for_first_word[char] += 1

        # iterate over the characters in t and check if the character is in the dictionary
        for char in t:
            # if the character is not in the dictionary, add 1 to the total_count
            if char not in dict_for_first_word:
                total_count += 1
            # if the character is in the dictionary, check if the count is 0
            else:
                # if the count is equal to 0 or less than, add 1 to the total_count
                if dict_for_first_word[char] <= 0:
                    total_count += 1
                # otherwise subtract 1 from the count
                else:
                    dict_for_first_word[char] -= 1

        # return the total_count
        return total_count
