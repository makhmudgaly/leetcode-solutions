from collections import defaultdict

class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        d = defaultdict(int)
        ans = set()
        
        for num in set(nums1):
            d[num]+=1
            if d[num] >=2:
                ans.add(num)
        for num in set(nums2):
            d[num]+=1
            if d[num] >=2:
                ans.add(num)
        
        for num in set(nums3):
            d[num]+=1
            if d[num] >=2:
                ans.add(num)
                
        return list(ans)
        