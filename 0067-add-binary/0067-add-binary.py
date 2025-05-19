class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a = int(a, 2)
        b = int(b, 2)

        while b != 0:
            x = a ^ b
            y = (a&b) << 1

            a, b = x, y

        return bin(a)[2:]
        
        