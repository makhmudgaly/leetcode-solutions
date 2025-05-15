class Solution:
    def rob(self, nums: List[int]) -> int:
        self.memo = {}
        n = len(nums)

        if n == 0 or nums is None:
            return 0

        if n == 1:
            return nums[0]

        return max(self.rob_from(0, n-1, nums), self.rob_from(1, n, nums))
    
    def rob_from(self, pos, limit, nums):
        if pos >= limit:
            return 0
        
        if (pos, limit) in self.memo:
            return self.memo[(pos, limit)]

        ans = max(
            self.rob_from(pos + 1, limit, nums), 
            self.rob_from(pos + 2, limit, nums) + nums[pos]
        )

        self.memo[(pos, limit)] = ans
        return ans

