from collections import defaultdict
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        d = defaultdict(int)
        ans = []
        n = len(nums) / 3
        for num in nums:
            d[num] += 1
        for k in d:
            if d[k] > n:
                ans.append(k)
                
        return ans