from collections import defaultdict
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        d = defaultdict(int)
        
        for num in nums:
            d[num] += 1
            
        min_v = 0
        max_v = 0
        
        for num in nums:
            if num < min_v:
                min_v = num
            if num > max_v:
                max_v = num
                
        for i in range(max_v):
            if i not in d and i > 0:
                return i
            
        return max_v + 1