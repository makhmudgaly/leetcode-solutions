class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        min_el = min(nums)
        max_el = max(nums)
        
        if len(nums) <= 2:
            return -1
        
        for num in nums:
            if min_el < num < max_el:
                return num
            
        return -1
        