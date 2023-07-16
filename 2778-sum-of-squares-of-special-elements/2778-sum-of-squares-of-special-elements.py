class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        ans = sum([nums[x]**2 for x in range(len(nums)) if len(nums) % (x+1) == 0])
        return ans