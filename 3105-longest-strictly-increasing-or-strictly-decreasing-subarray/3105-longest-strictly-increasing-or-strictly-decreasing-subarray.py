class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        max_inc = 0
        max_dec = 0
        
        # Check for increasing
        for i in range(0,len(nums)):
            inc = 1
            prev = nums[i]
            for j in range(i+1, len(nums)):
                if nums[j] <= prev:
                    break
                inc += 1
                prev = nums[j]
            max_inc = max(max_inc, inc)
        
        # Check for decreasing
        for i in range(0,len(nums)):
            dec = 1
            prev = nums[i]
            for j in range(i+1, len(nums)):
                if nums[j] >= prev:
                    break
                dec += 1
                prev = nums[j]
            max_dec = max(max_dec, dec)
            
        
            
        
        return max(max_inc, max_dec)
            