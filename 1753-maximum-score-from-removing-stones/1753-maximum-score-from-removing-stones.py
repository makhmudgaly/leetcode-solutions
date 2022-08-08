class Solution:
    def maximumScore(self, a: int, b: int, c: int) -> int:
        all_zero = (a+b+c) // 2
        two_empty = a+b+c - max(a,b,c)
        return min(all_zero, two_empty)