from collections import defaultdict
class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        d = defaultdict(int)
        ans = 0
        for num in nums:
            d[num] += 1
            if d[num] == 2:
                ans ^= num
        return ans
        
        