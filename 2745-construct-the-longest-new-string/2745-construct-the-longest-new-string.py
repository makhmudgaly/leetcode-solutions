class Solution:
    def longestString(self, x: int, y: int, z: int) -> int:
        # BBAABBAABBAB
        mn = min(x, y)
        if x == y:
            return 4 * x + 2 * z
        
        return 2 * mn + (mn + 1) * 2 + 2 * z