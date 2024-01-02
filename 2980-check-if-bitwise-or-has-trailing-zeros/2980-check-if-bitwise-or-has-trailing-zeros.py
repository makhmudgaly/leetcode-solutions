class Solution:
    def hasTrailingZeros(self, nums: List[int]) -> bool:
        even = 0
        for num in nums:
            if num & 1 == 0:
                even += 1
        
        return True if even >=2 else False