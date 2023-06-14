class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        ans = 0
        while k > 0:
            max_el = max(nums)
            ans += max_el
            nums.append(max_el + 1)
            nums.remove(max_el)
            k-=1
        
        return ans