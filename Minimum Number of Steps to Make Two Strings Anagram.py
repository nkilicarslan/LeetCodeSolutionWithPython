class Solution:
    def minSteps(self, s: str, t: str) -> int:
        total_count = 0
        dict_for_first_word = {}
        for char in s:
            if char not in dict_for_first_word:
                dict_for_first_word[char] = 1
            else:
                dict_for_first_word[char] += 1

        for char in t:
            if char not in dict_for_first_word:
                total_count += 1
            else:
                if dict_for_first_word[char] <= 0:
                    total_count += 1
                else:
                    dict_for_first_word[char] -= 1

        return total_count