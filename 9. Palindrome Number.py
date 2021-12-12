class Solution:
    def isPalindrome(self, x: int) -> bool:
        str_input = str(x)
        str_len = len(str_input)
        for i in range(int(str_len/2)+1):
            if str_input[i] == str_input[str_len-1-i]:
                continue
            else:
                return False
        return True
"""
more cooler and faster but at the same time more memory usage way:
class Solution:
    def isPalindrome(self, x: int) -> bool:
        str_x = str(x)
        return str_x == str_x[::-1]
"""