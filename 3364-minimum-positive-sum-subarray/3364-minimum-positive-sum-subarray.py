class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        
        n = len(nums)
        min_sum = inf
        prefix = [0] * (n+1)
        prefix[0] = nums[0]
        
        
        for idx in range(1, n+1):
            prefix[idx] += nums[idx-1] + prefix[idx - 1]
        
        for left in range(n):
            for right in range(left+1, n+1):
                curr_sum, length = prefix[right] - prefix[left], right - left
                if l <= length <= r and 0 < curr_sum < min_sum:
                    min_sum = curr_sum
        
        return -1 if min_sum == inf else min_sum
                    
        
        