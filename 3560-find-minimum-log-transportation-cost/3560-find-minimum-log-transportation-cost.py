class Solution:
    def minCuttingCost(self, n: int, m: int, k: int) -> int:
        if m <= k and n <=k:
            return 0
        
        longer = max(n,m)
        cuts = longer - k

        return cuts * k