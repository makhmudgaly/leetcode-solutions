class Solution:
    def vowelConsonantScore(self, s: str) -> int:
        vowel_set = ('a','e', 'i', 'o', 'u')
        v = 0
        n = 0
        for ch in s:
            if ch.isalpha():
                n += 1

            if ch in vowel_set:
                v += 1
        
        c = n - v

        if c > 0:
            return math.floor(v/c)
        
        return 0