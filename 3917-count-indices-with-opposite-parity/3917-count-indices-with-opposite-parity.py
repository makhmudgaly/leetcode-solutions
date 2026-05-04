class Solution:
    def countOppositeParity(self, nums: list[int]) -> list[int]:
        res = []
        for i in range(len(nums)):
            is_odd = nums[i] % 2 == 0
            count = 0
            for j in range(i + 1, len(nums)):
                count += is_odd != (nums[j] % 2 == 0)
            
            res.append(count)
        
        return res