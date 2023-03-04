class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(haystack) < len(needle):
            return -1
        
        if haystack == needle:
            return 0
        
        for left in range(len(haystack)-len(needle)+1):
            for right in range(len(needle)):
                if haystack[left+right] != needle[right]:
                    break
            else:
                return left
            
        return -1