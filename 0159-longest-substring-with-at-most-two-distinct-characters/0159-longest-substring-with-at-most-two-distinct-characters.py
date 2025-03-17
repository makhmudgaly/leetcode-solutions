from collections import defaultdict
class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        counter = defaultdict(int)
        n = len(s)
        left = 0
        ans = 1
        for right in range(n):
            counter[s[right]] += 1
            
            if len(counter) <= 2:
                
                ans = max(ans, right - left + 1)
            else:
                counter[s[left]] -= 1
                if counter[s[left]] == 0:
                    del counter[s[left]]
                left += 1
            
        return ans