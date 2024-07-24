class Solution:
    def minChanges(self, n: int, k: int) -> int:
        if n == k:
            return 0
        
        n = bin(n)[2:]
        k = bin(k)[2:]
        fill_zeroes = max(len(n), len(k))
        k = k.zfill(fill_zeroes)
        n = n.zfill(fill_zeroes)
        
        ans = 0
        t = ""
        for idx, dig in enumerate(n):
            if dig == '1' and k[idx] == '0':
                t+="0"
                ans += 1
            else:
                t+=dig
        
        return ans if t == k else -1