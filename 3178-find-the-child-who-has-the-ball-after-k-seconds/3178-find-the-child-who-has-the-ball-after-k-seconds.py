class Solution:
    def numberOfChild(self, n: int, k: int) -> int:
        n = n-1
        rounds, mod = divmod(k,n)
        if rounds & 1 == 0:
            return mod
        return n-mod
            