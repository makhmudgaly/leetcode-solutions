from collections import defaultdict
class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        n = len(nums)
        total = (n * (n-1)) // 2
        good = 0
        d = defaultdict(int)
        for i in range(n):
            good += d[nums[i] -i]
            d[nums[i]-i]+=1
        return (total - good)
            