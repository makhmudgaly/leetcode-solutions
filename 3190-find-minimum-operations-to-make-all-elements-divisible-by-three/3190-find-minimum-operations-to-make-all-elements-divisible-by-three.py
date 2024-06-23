class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        ans = 0 
        for i in range(len(nums)):
            ans += min(nums[i]%3, 3 - (nums[i]%3))
        return ans