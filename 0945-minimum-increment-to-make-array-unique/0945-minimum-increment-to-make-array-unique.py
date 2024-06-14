class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        ans = 0
        
        for i in range(1, len(nums)):
            if nums[i] <= nums[i-1]:
                incr = nums[i-1] + 1 - nums[i]
                ans += incr
                
                nums[i] = nums[i-1] + 1
        
        return ans
        