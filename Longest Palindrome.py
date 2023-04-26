class Solution:
    def longestPalindrome(self, s: str) -> int:
        letter_dp = {}
        add_one = False
        count = 0
        for char in s:
            if char not in letter_dp:
                letter_dp[char] = 1
            else:
                letter_dp[char] += 1
        if len(letter_dp.items()) == 1:
            return len(s)
        else:
            for value in letter_dp.values():
                if value % 2 == 0:
                    count += value
                else:
                    count += value - 1
                    add_one = True

        if add_one == True:
            return count + 1
        return count
