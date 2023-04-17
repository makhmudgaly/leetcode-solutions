class Solution:
    def maxDivScore(self, nums: List[int], divisors: List[int]) -> int:
        ans = (-1, -1)
        for div in sorted(divisors):
            score = 0
            for num in nums:
                if num % div == 0:
                    score += 1
            
            if score > ans[1]:
                ans = (div, score)
        
        return ans[0]