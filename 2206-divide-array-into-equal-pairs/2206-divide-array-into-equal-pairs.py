from collections import defaultdict
class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        d = defaultdict(int)
        for num in nums:
            d[num] += 1
            
        for k,v in d.items():
            if v % 2 != 0:
                return False
        
        return True