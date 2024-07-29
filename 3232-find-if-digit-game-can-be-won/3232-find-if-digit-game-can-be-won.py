class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        totalSum = sum(nums)
        single_digit = 0
        for num in nums:
            if 1 <= num <= 9:
                single_digit += num
        
        return single_digit != (totalSum - single_digit)