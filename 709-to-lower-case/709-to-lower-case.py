class Solution:
    def toLowerCase(self, s: str) -> str:
        print(ord('a'), ord('z'))
        dict = {}
        ans = ""
        for i in range(26):
            dict[ord('A') + i] = chr(ord('a') + i)
        
        for ch in s:
            if ch >= 'A' and ch<='Z':
                ans+=dict[ord(ch)]
            else:
                ans+=ch
        
        return ans
        
        
        