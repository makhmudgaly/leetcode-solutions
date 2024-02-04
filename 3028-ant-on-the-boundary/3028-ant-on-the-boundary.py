class Solution:
    def returnToBoundaryCount(self, nums: List[int]) -> int:
        curr, ans = 0, 0
        for num in nums:
            curr += num
            if curr == 0:
                ans += 1
        
        return ans