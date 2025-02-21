class Solution:
    def longestCommonPrefix(self, s: str, t: str) -> int:
        left = 0
        right = 0
        used_removal = False
        longest_prefix = 0
        while left < len(s) and right < len(t):
            print(s[left], t[right])
            if s[left] == t[right]:
                left += 1
                right += 1
                longest_prefix += 1
            elif used_removal:
                return longest_prefix
            else:
                used_removal = True
                left += 1
        
        return longest_prefix
