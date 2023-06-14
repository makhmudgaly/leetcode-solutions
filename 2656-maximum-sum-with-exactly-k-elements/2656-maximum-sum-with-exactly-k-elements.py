class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        ans = 0
        max_el = max(nums)
        while k > 0:
            
            ans += max_el
            max_el += 1
            k-=1
        
        return ans