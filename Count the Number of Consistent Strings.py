class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        # create a dictionary to store the allowed characters
        dict_for_allowed = {}
        # create a variable to store the total count
        total_count = 0

        # iterate over the allowed string and add the characters to the dictionary
        for char in allowed:
            dict_for_allowed[char] = 1

        # iterate over the words
        for word in words:
            # add 1 to the total count
            total_count += 1
            # iterate over the characters of the word
            for char in word:
                # if the character is not in the dictionary, subtract 1 from the total count and break
                if char not in dict_for_allowed:
                    total_count -= 1
                    break

        # return the total count
        return total_count
