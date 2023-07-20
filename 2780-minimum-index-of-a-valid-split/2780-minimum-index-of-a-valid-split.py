from collections import defaultdict
class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        dominant, freq = 0, defaultdict(int)
        ans = 0
        for num in nums:
            freq[num] += 1
            if freq[num] * 2 > len(nums):
                dominant = num
        f1 = 0
        for idx in range(0, len(nums)):
            
            if nums[idx] == dominant:
                f1 += 1
            f2 = freq[dominant] - f1
            
            if f1 * 2 > (idx + 1) and f2 * 2 > len(nums) - idx - 1:
                return idx
           
        return -1
            