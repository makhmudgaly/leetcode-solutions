class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        prefix_sum = nums[0]
        max_prefix = prefix_sum
        right = 0
        d = Counter(nums)
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1] + 1:
                break
                
            prefix_sum += nums[i]
            max_prefix = max(prefix_sum, prefix_sum)
        
        for missing_value in range(max_prefix, 2*max_prefix+51):
            if missing_value not in d:
                return missing_value
        
        return max_prefix