class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        d = {}
        ans = -1
        for idx, ch in enumerate(s):
            if ch in d:
                ans = max(ans, idx - d[ch]-1)
            else:
                d[ch] = idx
        
        return ans