from collections import defaultdict
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        d = defaultdict(int)
        
        for num in nums:
            d[num] += 1
            if d[num] == 3:
                del d[num]
        
        return list(d.keys())[0]