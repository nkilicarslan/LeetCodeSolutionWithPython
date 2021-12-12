class Solution:
    def reverse(self, x: int) -> int:
        reversed_string = str(str(x)[::-1])
        if reversed_string[0] == '0' and len(reversed_string)>1:
            reversed_string = reversed_string[1:]
        reversed_string = int(reversed_string)
        return reversed_string
    reverse(1,12)