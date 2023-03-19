class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # convert a to integer with built-in function int()
        a = int(a, 2)
        # convert b to integer with built-in function int()
        b = int(b, 2)
        # add a and b
        c = a + b
        # convert c to binary
        c = bin(c)
        # return the binary string
        return c[2:]
