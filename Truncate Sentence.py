class Solution:
    # this function will return the truncated sentence
    def truncateSentence(self, s: str, k: int) -> str:
        # split the string into a list of words and return the first k words with joining them with a space
        return ''.join(s.split()[:k])
