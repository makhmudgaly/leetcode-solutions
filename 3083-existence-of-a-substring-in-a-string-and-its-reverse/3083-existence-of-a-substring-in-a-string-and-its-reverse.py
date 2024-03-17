class Solution:
    def isSubstringPresent(self, s: str) -> bool:
        reverse = s[::-1]
        
        for st in range(0, len(s)-1):
            cand = s[st:st+2]
            if cand in reverse:
                return True
        
        return False