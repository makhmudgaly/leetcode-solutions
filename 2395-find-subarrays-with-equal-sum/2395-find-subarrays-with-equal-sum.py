from collections import defaultdict

class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        d = defaultdict(int)
        for idx in range(len(nums)-1):
            s = nums[idx] + nums[idx+1]
            d[s] += 1

        for key in d:
            if d[key] >= 2:
                return True
        
        return False