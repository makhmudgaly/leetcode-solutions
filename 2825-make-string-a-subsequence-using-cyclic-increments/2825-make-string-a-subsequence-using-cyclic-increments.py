class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        left = 0
        right = 0
        ans = 0
        
        while left < len(str1) and right < len(str2):
            if str1[left] == str2[right]:
                left += 1
                right += 1
                ans += 1
            elif chr((((ord(str1[left]) - 97 + 1)%26) + 97)) == str2[right]:
                left += 1
                right += 1
                ans += 1
            else:
                left += 1
                
        
        return ans == len(str2)