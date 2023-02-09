from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = defaultdict(int)
        for num in nums:
            d[num] += 1
        
        ans = [x[0] for x in sorted(d.items(), key=lambda x: x[1], reverse=True)[:k]]
        
        return ans
        