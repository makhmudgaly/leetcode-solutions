class Solution:

    def rob(self, nums: List[int]) -> int:
        self.memo = {}
        return self.rob_from(0, nums)
    
    def rob_from(self, pos, nums):
        if pos >= len(nums):
            return 0
        
        if pos in self.memo:
            return self.memo[pos]
        
        ans = max(
            self.rob_from(pos + 1, nums), # do not rob, check next
            self.rob_from(pos + 2, nums) + nums[pos] # rob curr, jump next available
        )

        self.memo[pos] = ans
        return ans