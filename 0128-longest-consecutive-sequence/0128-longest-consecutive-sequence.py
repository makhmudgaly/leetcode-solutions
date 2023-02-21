from collections import defaultdict

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        ans = 0
        for n in nums:
            if (n - 1) not in nums:
                window = 1
                while n + window in nums:
                    window += 1
                ans = max(ans, window)
        
        return ans
            
        
        