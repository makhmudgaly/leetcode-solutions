class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        d = Counter(nums)
        ans = 0

        for x in d:
            if k > 0 and x + k in d:
                ans += 1
            elif k == 0 and d[x] > 1:
                ans += 1
        
        return ans
