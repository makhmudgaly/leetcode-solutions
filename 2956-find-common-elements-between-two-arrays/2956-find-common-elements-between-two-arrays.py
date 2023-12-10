from collections import defaultdict
class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = [0, 0]
        d1, d2 = defaultdict(int), defaultdict(int)
        
        for num in nums1:
            d1[num] += 1
            
        for num in nums2:
            d2[num] += 1
        
        for k, v in d1.items():
            if k in d2:
                ans[0] += v
                ans[1] += d2[k]
        
        return ans