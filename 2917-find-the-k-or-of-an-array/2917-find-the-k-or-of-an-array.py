class Solution:
    def findKOr(self, nums: List[int], k: int) -> int:
        ans = 0
        
        for bit in range(32):
            count = 0
            for num in nums:
                
                if num & (2 ** bit) == (2 ** bit):
                    count += 1
            if count >= k:
                ans += 2 ** bit
        
        return ans