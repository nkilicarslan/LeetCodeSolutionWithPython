class Solution:
    # this function will return the length of the longest possible palindrome
    def longestPalindrome(self, s: str) -> int:
        # create a dictionary to store the letter and the number of times it appears in the string
        letter_dp = {}
        # create a flag to check if there is letter that appears an odd number of times
        add_one = False
        # create a variable to store the length of the letters
        count = 0
        # iterate over the string
        for char in s:
            # if the letter is not in the dictionary, add it to the dictionary
            if char not in letter_dp:
                letter_dp[char] = 1
            # otherwise increment the value of the letter by 1
            else:
                letter_dp[char] += 1
        # if there is only one letter in the dictionary, return the length of the string
        if len(letter_dp.items()) == 1:
            return len(s)
        # otherwise iterate over the values of the dictionary
        else:
            for value in letter_dp.values():
                # if the value is even, add it to the count
                if value % 2 == 0:
                    count += value
                # otherwise add the value - 1 to the count
                else:
                    count += value - 1
                    add_one = True
        # if add_one is True, add 1 to the count
        if add_one == True:
            return count + 1
        # otherwise return the count
        return count
