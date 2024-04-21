from collections import defaultdict
from string import ascii_lowercase

class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        count = 0
        d = defaultdict(int)
        for ch in word:
            d[ch] += 1
        
        for letter in ascii_lowercase:
            if letter in d and letter.upper() in d:
                count += 1
        
        return count
        
        