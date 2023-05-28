class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        dict_for_allowed = {}
        total_count = 0

        for char in allowed:
            dict_for_allowed[char] = 1

        for word in words:
            total_count += 1
            for char in word:
                if char not in dict_for_allowed:
                    total_count -= 1
                    break

        return total_count