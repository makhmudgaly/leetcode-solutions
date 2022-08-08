class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor = 0
        for i in nums:
            xor ^= i
            
        last_bit = xor & (-xor)
        
        first = 0
        for i in nums:
            if i & last_bit == 0:
                first ^= i
            
        return [first, first^xor]