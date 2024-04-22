class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        lowers = [-1]*26
        uppers = [-1]*26
        ans = 0
        
        for idx ,ch in enumerate(word):
            if ch.isupper() and uppers[ord(ch)-ord('A')] == -1:
                uppers[ord(ch)-ord('A')] = idx
            if ch.islower():
                lowers[ord(ch)-ord('a')] = idx
        
        for i in range(26):
            if (lowers[i] != -1 and uppers[i] != -1) and (lowers[i] < uppers[i]):
                ans += 1
        
        return ans