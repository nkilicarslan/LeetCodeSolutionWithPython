class Solution:
    def longestPalindrome(self, s: str) -> int:
        letter_dp = {}
        count = 0
        is_one = False
        for char in s:
            if char not in letter_dp:
                letter_dp[char] = 1
            else:
                letter_dp[char] += 1
        values_of_letter_dp = list(letter_dp.values())
        for value in values_of_letter_dp:
            if value % 2 == 0:
                count += value
            else:
                count += value - 1
                if count == 1:
                    is_one = True
        if 1 in values_of_letter_dp or is_one:
            return count + 1
        else:
            return count
a = Solution()
a.longestPalindrome("abccccdd")