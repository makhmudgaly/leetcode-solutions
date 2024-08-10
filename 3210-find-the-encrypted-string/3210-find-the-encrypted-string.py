class Solution:
    def getEncryptedString(self, s: str, k: int) -> str:
        ans = ""
        n = len(s)
        for i,ch in enumerate(s):
            kth = (i + k) % n
            ans += s[kth]
        return ans