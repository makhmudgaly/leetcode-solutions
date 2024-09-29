class Solution:
    def minElement(self, nums: List[int]) -> int:
        ans = float("inf")
        for num in nums:
            digit_sum = sum(int(digit) for digit in str(num))
            ans = min(digit_sum, ans)
        
        return ans