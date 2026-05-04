class Solution:
    def validDigit(self, n: int, x: int) -> bool:
        seen = set()

        while n > 0:
            f = n % 10
            n = n // 10
            seen.add(f)
        
        return x in seen and f != x