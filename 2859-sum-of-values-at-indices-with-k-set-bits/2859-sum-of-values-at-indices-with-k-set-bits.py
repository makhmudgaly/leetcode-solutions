class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        ans = 0
        for idx, num in enumerate(nums):
            ones = bin(idx)[2:].count('1')
            if ones == k:
                ans += num
        return ans