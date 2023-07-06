class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        ans = len(nums) + 1
        left = 0
        window = 0
        
        for right in range(len(nums)):
            window += nums[right]
        
            while window >= target:
                ans = min(right - left + 1, ans)
                window -= nums[left]
                left += 1
        return 0 if ans == len(nums) + 1 else ans
        