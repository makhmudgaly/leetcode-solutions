class Solution:
    def greatestLetter(self, s: str) -> str:
        dict = {}
        for ch in s:
            dict[ch] = 1
        
        ans = ""
        
        for i in range(90,64,-1):
            ch = chr(i)
            if ch in dict and ch.lower() in dict:
                ans=ch
                break
        return ans
        