import math

class Solution:
    def countBeautifulPairs(self, nums: List[int]) -> int:
        ans = 0
        
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                first = int(str(nums[i])[0])
                last  = int(str(nums[j])[-1])
                if math.gcd(first, last) == 1:
                    ans += 1
        
        
        return ans