class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        count = 0
        dict = {
            ' ': ' '
        }
        for ch in key:
            if ch in dict:
                continue 
            dict[ch] = chr(ord('a') + count)
            count+=1
        ans = ""
        for ch in message:
            ans+=dict[ch]
            
        return ans
        