class Solution:
    # this function will return true if the two string arrays are equivalent
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        # create two variables to store the strings
        string1 = ""
        string2 = ""

        # iterate over the words and add them to the strings
        for word in word1:
            string1 += word

        # iterate over the words and add them to the strings
        for word in word2:
            string2 += word

        # return true if the strings are equal
        return string2 == string1
