class Solution:
    def maxScore(self, nums: List[int]) -> int:
        nums = sorted(nums, reverse=True)
        ans = 0
        pref = 0
        for num in nums:
            pref += num
            if pref > 0:
                ans += 1
        
        return ans