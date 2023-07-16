from collections import Counter

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        counter_nums1 = Counter(nums1)
        counter_nums2 = Counter(nums2)
        
        ans = []
        for key, val in counter_nums1.items():
            if key in counter_nums2:
                ans.extend([key]*min(val, counter_nums2[key]))
        
        return ans